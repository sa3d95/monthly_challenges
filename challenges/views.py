from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january" : "Make 10 push ups a day !!!",    
    "february" : "Plant a tree !!",
    "march" : "Learn 1 hour of Django !!",
    "april" : "Help your brother solve a math problem !!",
    "may" : "Pick a book and read about 30 pages of it !!",
    "june" : "Start searching about the history of Islam !!",
    "july" : "Make yourself a healthy meal !!",
    "august" : "Help some of your relatives with your money !!",
    "september" : "Revise the holy quran for the entire month",
    "october" : "Pray all prayers in the mosque !!",
    "november" : "Teach something to someone for free !!",
    "december" : "Help someone in need !!"
}

# Create your views here.

def monthly_challenges_with_numbers(request, month):
    try:
        all_months = list(monthly_challenges.keys())
        redirected_month = all_months[month-1]
        #redirected_path = reverse("x", args=[redirected_month]) #why it is not working?!!!
        return HttpResponseRedirect(redirected_month)

    except Exception:
        return HttpResponseNotFound("Invalid Month number !!!")
    
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)

    except Exception:
        return HttpResponseNotFound("Invalid Month !!!")
    

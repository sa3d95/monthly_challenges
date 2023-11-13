from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    
    if month == "january":
        challenge_text = HttpResponse("Make 10 push ups a day !!!")
    elif month == "february":
        challenge_text = HttpResponse("Make 10 pull ups a day !!!")
    elif month == "march":
        challenge_text = HttpResponse("Make 10 more prayers than usual !!!")
    else:
        return HttpResponseNotFound("Not a valid month !!!")
    return HttpResponse(challenge_text)
    

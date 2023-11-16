from django.urls import path
from challenges import views


urlpatterns = [
    path("<int:month>", views.monthly_challenges_with_numbers),
    path("<str:month>", views.monthly_challenge, name="x")    
]
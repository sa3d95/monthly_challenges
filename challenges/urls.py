from django import views
from django.urls import path

from monthly_challenges.challenges import views


urlpatterns = [
    path("january", views.index),
]



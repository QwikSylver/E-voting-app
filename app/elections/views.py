from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import *


def HomePageView(response):
    return HttpResponse("Home Page")


def UserProfileView(response, user_id):
    try:
        user = Voter.objects.get(voter_id=user_id)
    except Voter.DoesNotExist:
        raise Http404("Voter does not exist")
    return render(response, "user_profile.html", {"user": user})

# from urllib import request
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *


def logoutUser(request):
    logout(request)
    return redirect("login")


def ResultsPageView(request, election_id):
    results = Vote.objects.filter(election_id=election_id)

    categories = Category.objects.all()

    context = {"results": results, "categories": categories}

    return render(request, "elections/elections/results.html", context)


@login_required(login_url="login")
def UserProfileView(request, user_id):

    try:
        user = Voter.objects.get(voter_id=user_id)
    except Voter.DoesNotExist:
        raise Http404("Voter does not exist")
    return render(request, "elections/user_profile.html", {"user": user})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = Voter.objects.get(voter_id=username)
        except:
            messages.error(request, "Incorrect Username or Password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Account is disabled")
        else:
            messages.error(request, "Username or Password Does Not Exist")

    return render(request, "registration/login.html", {})


@login_required(login_url="login")
def electionsPage(request):
    elections = Election.objects.all()
    context = {"elections": elections}
    return render(request, "elections/elections/elections.html", context)


@login_required(login_url="login")
def electionDetails(request, election_id):
    election = Election.objects.get(election_id=election_id)
    categories = Category.objects.filter(election=election_id)
    context = {"election": election, "categories": categories}
    return render(request, "elections/elections/election_details.html", context)


@login_required(login_url="login")
def categoryDetails(request, category_id):
    category = Category.objects.get(category_id=category_id)
    candidates = Candidate.objects.filter(candidate_category=category_id)

    candidate = None

    election = category.election

    if request.method == "POST":
        candidate = Candidate.objects.get(candidate_id=request.POST.get("candidate_id"))

        # get id of user currently logged in
        voter = Voter.objects.get(voter_id=request.user.voter_id)

        # cast vote
        vote = Vote.objects.create(
            voter_id=voter, candidate_id=candidate, election_id=election
        )
        vote.save()

        return redirect("elections_details", election_id=election.election_id)

    context = {"category": category, "candidates": candidates}
    return render(request, "elections/elections/category.html", context)

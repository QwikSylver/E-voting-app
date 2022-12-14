# from urllib import request
import datetime
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from .models import *


def logoutUser(request):
    logout(request)
    return redirect("login")


def ResultsPageView(request, election_id):
    results = Vote.objects.filter(election_id=election_id)

    categories = Category.objects.all()

    context = {"results": results, "categories": categories}

    return render(request, "elections/elections/results.html", context)


@method_decorator(login_required, name="dispatch")
class UserProfileView(UpdateView):
    model = Voter
    fields = ["username"]
    template_name_suffix = "_update_profile"


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


def ElectionResults(request, election_id):
    election = Election.objects.get(election_id=election_id)
    categories = Category.objects.filter(election=election_id)
    canditates = Candidate.objects.filter(candidate_category__in=categories)
    for cadidate in canditates:
        print(cadidate.candidate_name, cadidate.candidate_category.category_id)
    votes = Vote.objects.filter(election_id=election_id).count()
    # candidate_votes = Vote.objects.raw("select candidate_id, count(voter_id) as votes from votes where election_id = %s and category_id = %s group by candidate_id", [election_id, categories.category_id])
    canditates_votes = (
        Vote.objects.filter(election_id=election_id)
        .values("candidate_id")
        .annotate(votes=models.Count("voter_id"))
    )
    context = {
        "election": election,
        "categories": categories,
        "votes": votes,
        "candidates": canditates,
        "canditates_votes": canditates_votes,
    }
    return render(request, "elections/election_results.html", context)


@login_required(login_url="login")
def electionsPage(request):
    elections = Election.objects.all()
    days_left = {}
    for election in elections:
        if (election.end_time - datetime.datetime.now(datetime.timezone.utc)).days > 0:
            days_left[election.election_id] = election.end_time - datetime.datetime.now(
                datetime.timezone.utc
            )
        else:
            days_left[election.election_id] = "over"

    context = {"elections": elections, "days_left": days_left}
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

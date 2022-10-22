from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from .models import *


def HomePageView(response):
    return HttpResponse("Home Page")

def UserProfileView(response, user_id):
    try:
        user = Voter.objects.get(id=user_id)
    except Voter.DoesNotExist:
        raise Http404("Voter does not exist")
    return render(response, "user_profile.html", {"user": user})

def electionsPage(request):
    elections = Election.objects.all()
    context = {'elections': elections}
    return render(request, "elections/elections/elections.html", context)

def electionDetails(request, election_id):
    election = Election.objects.get(election_id=election_id)
    categories = Category.objects.filter(election=election_id)
    context = {'election': election, 'categories': categories}
    return render(request, "elections/elections/election_details.html", context)

def categoryDetails(request, category_id):
    category = Category.objects.get(category_id=category_id)
    candidates = Candidate.objects.filter(candidate_category=category_id)
    
    candidate = None
    voter = None
    election = category.election

    # Does not work
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate_id')
        candidate = Candidate.objects.get(candidate_id=candidate_id)
        voter = Voter.objects.create(voter_id='sakaria26')
        vote = Vote.objects.create(voter_id=voter, election_id=election, candidate_id=candidate)
        print(vote)
        vote.save()
            
        return redirect('category_details', category_id=category_id)

    context = {'category': category, 'candidates': candidates}
    return render(request, "elections/elections/category.html", context)
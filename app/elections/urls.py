from django.urls import path

from .views import (
    HomePageView,
    UserProfileView,
    electionsPage,
    electionDetails,
    categoryDetails,
)


urlpatterns = [
    path("elections/", electionsPage, name="home"),
    path("elections/<str:election_id>", electionDetails, name="elections_details"),
    path("user_profile/<str:user_id>", UserProfileView, name="user_profile"),
    path("categories/<str:category_id>", categoryDetails, name="category_details"),
]

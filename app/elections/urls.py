from django.urls import path

from .views import (
    UserProfileView,
    electionsPage,
    electionDetails,
    categoryDetails,
    ResultsPageView,
    logoutUser,
    loginPage,
    ElectionResults
)


urlpatterns = [
    path("login/", loginPage, name="login"),
    path("logout/", logoutUser, name="logout"),
    path("elections/", electionsPage, name="home"),
    path("elections/<str:election_id>", electionDetails, name="elections_details"),

    path("elections/<str:election_id>/results", ElectionResults, name="elections_results"),
    path("user_profile/<str:pk>", UserProfileView.as_view(), name="user_profile"),
    path("categories/<str:category_id>", categoryDetails, name="category_details"),
]

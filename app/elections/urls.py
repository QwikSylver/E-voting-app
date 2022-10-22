from django.urls import path

from .views import HomePageView, UserProfileView, elections


urlpatterns = [
    path("", HomePageView, name="home"),
    path("user_profile/<str:user_id>", UserProfileView, name="user_profile"),
    path("elections/", elections, name="elections"),
]

from django.urls import path

from .views import HomePageView, UserProfileView


urlpatterns = [
    path("", HomePageView, name="home"),
    path("user_profile/<int:user_id>", UserProfileView, name="user_profile"),
]

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


from .models import Voter


class VoterCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Voter
        fields = ("username",)


class VoterChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Voter
        fields = ("username",)

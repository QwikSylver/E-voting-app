from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Election, Vote, Voter, Candidate, Category
from .forms import VoterChangeForm, VoterCreationForm


class VoterAdmin(UserAdmin):
    add_form = VoterCreationForm
    form = VoterChangeForm
    model = Voter
    list_display = [
        "username",
        "email",
        "is_staff",
    ]


# Register your models here.
admin.site.register(Vote)
admin.site.register(Voter)
admin.site.register(Candidate)
admin.site.register(Category)
admin.site.register(Election)

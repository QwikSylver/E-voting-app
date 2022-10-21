from django.contrib import admin
from .models import Election, Vote, Voter, Candidate, Category

# Register your models here.
admin.site.register(Vote)
admin.site.register(Voter)
admin.site.register(Candidate)
admin.site.register(Category)
admin.site.register(Election)

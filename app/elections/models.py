from django.contrib.auth.models import AbstractUser
import uuid

from django.db import models


# Create your models here.
class Election(models.Model):
    election_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    election_reason = models.CharField(max_length=100)
    voters = models.ManyToManyField("Voter", related_name="elections")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.election_reason


class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic = models.CharField(max_length=100)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic


class Candidate(models.Model):
    candidate_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    candidate_name = models.CharField(max_length=100)
    candidate_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.candidate_name


class Voter(AbstractUser):
    voter_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username


class Vote(models.Model):
    voter_id = models.ForeignKey(Voter, on_delete=models.CASCADE)
    election_id = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.voter_id

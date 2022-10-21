from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_reason = models.CharField(max_length=100)

    def __str__(self):
        return self.election_reason


class Election(models.Model):
    election_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=100)
    elections = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic


class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    candidate_name = models.CharField(max_length=100)
    candidate_election = models.ForeignKey(Election, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.candidate_name


class Voter(models.Model):
    voter_id = models.AutoField(primary_key=True)
    voter_password = models.CharField(max_length=100)

    def __str__(self):
        return self.voter_id


class Vote(models.Model):
    voter_id = models.ForeignKey(Voter, on_delete=models.CASCADE)
    election_id = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.vote_id

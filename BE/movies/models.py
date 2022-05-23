from django.db import models
from django.conf import settings
import datetime


class Genre(models.Model):
    name = models.CharField(max_length=300, null=False)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=300, null=False)
    profile_path = models.TextField(null=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    title = models.CharField(max_length=300)
    overview = models.TextField()
    budget = models.BigIntegerField()
    popularity = models.FloatField()
    poster_path = models.TextField(null=True)
    release_date = models.DateField(null=True, default=datetime.date.today)
    revenue = models.BigIntegerField()
    runtime = models.IntegerField(null=True)
    tagline = models.TextField(null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    words = models.TextField(null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    
    def __str__(self):
        return self.title


    

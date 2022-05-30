from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
import datetime


class Actor(models.Model):
    name = models.CharField(max_length=50, null=False)
    profile_path = models.TextField(null=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class MoodTag(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class CaseTag(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies')
    moodtag = models.ManyToManyField(MoodTag, related_name='movies')
    casetag = models.ManyToManyField(CaseTag, related_name='movies')
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


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    review = models.TextField(null=True)

    def __str__(self):
        return self.user
    

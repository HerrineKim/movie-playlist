from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'overview', 'words', 'like_users', 'release_date', 'genres', 'poster_url', )



admin.site.register(Movie)
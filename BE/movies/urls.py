from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # actor
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),
    # movie
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/like/', views.like_movie),
]
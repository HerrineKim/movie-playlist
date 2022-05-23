from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # actor
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),

    # genre
    path('genres/<int:genre_pk>/', views.genre_detail),

    # movie
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/like/', views.like_movie),
    path('<int:user_pk>/recommendation/', views.user_like_movie),
    path('<int:movie_pk>/similar/', views.similar_movie), 
]
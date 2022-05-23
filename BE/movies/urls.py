from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # actor
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),

]
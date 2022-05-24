from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # articles
    path('', views.article_list_or_create),
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    path('<int:article_pk>/like/', views.like_article),
   
    # comments
    path('<int:article_pk>/comments/', views.create_comment),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
]
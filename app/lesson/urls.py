from django.urls import path

from . import views


app_name = 'lesson'

urlpatterns = [
    path('', views.list_excercise_article, name='list_excercise_articles'),
    path('<int:pk>/', views.view_excercise_article, name='excercise_article'),
    path('art/', views.view_sample_excercise_article, name='excercise1'),
    path('create', views.create_excercise_article, name='create'),
]

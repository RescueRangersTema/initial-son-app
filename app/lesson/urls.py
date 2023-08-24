from django.urls import path

from . import views


app_name = 'lesson'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.view_excercise_article, name='excercise'),
    path('art/', views.view_sample_excercise_article, name='excercise1'),
    path('create', views.create_excercise_article, name='create'),
]

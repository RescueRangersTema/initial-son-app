from django.urls import path

from . import views


app_name = 'lesson'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.view_excercise_article, name='excercise'),
    path('create', views.create_excercise_article, name='create'),
]

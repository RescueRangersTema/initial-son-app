from django.urls import path

from . import views


app_name = 'lesson'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.view_lesson_article, name='article'),
    path('create', views.create_lesson_article, name='create'),
]

from django.urls import path

from . import views


app_name = 'article'

urlpatterns = [
    path('page/<int:page>/', views.list_excercise_article, name='list_excercise_articles'),
    path('<int:pk>/', views.view_excercise_article, name='excercise_article'),
    # path('art/', views.view_sample_excercise_article, name='excercise1'),
    path('add-article/', views.create_excercise_article, name='create'),
    path('update-article/<int:pk>', views.update_excercise_article, name='update-article'),
    path('add-tag/', views.add_tag, name='add-tag'),
    
    path('add-excercise/', views.add_excercise, name='add-excercise'),
    path('update-excercise/<int:pk>', views.update_excercise, name='update-excercise'),
    path('excercise/page/<int:page>/', views.list_excercise, name='list_excercise'),
]

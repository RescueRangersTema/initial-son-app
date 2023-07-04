from django.urls import path

from . import views


app_name = 'account'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('signup/', views.sign_up, name='sign-up'),
]

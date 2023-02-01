from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('viewusers/', views.find_user, name='find_user'),
    path('userprofile/', views.user_profile, name='user_profile'),
    path('userrepository/', views.user_repository, name='user_repository'),
]
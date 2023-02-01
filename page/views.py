from django.shortcuts import render
from django.shortcuts import render, redirect
import requests


def home(request):
    return render(request, 'page/home.html')

# FIND USER

def find_user(request):
    number = request.GET.get('number')

    url1 = f"https://api.github.com/users?since={number}"
    response = requests.get(url1)
    data = response.json()
    context = {
        'data': data
    }

    return render(request, 'page/find_user.html', context)




# USER PROFILE

def user_profile(request):
    username = request.GET.get('username')
    url2 = f"https://api.github.com/users/{username}"
    response = requests.get(url2)
    data = response.json()
    context = {
        'data': data
    }

    return render(request, 'page/user_profile.html', context)


# USER REPOSITORY

def user_repository(request):
    user = request.GET.get('user')
    url3 = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url3)
    data = response.json()
    context = {
        'data': data
    }

    return render(request, 'page/user_repository.html', context)


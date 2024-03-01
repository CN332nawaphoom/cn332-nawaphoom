from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "account/login.html")

def logout_views(request):
    logout(request)
    return redirect('/')

def dashboard(request):
    context = {'test_word': "hello_world"}

    return render(request, "main/dashboard.html", context)
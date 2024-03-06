from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render, redirect ,HttpResponseRedirect 


@login_required(login_url='login')
def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")

@login_required(login_url='login')
def dashboard(request):
    context = {'test_word': "hello_world"}
    return render(request, "dashboard.html", context)

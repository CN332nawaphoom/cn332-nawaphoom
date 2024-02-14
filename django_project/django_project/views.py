from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def dashboard(request):
    context = {'test_word': "hello_world"}

    return render(request, "dashboard.html", context)
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



#@login_required(login_url='login')
#def index(request):
#    return render(request, "main/index.html")


def login(request):
    return render(request, "account/login.html")

def logout_views(request):
    logout(request)
    return redirect('/')

@login_required
def dashboard(request):
    context = {'test_word': "hello_world"}

    return render(request, "main/dashboard.html", context)


@login_required
def profile(request):

    return render(request, "main/profile.html")


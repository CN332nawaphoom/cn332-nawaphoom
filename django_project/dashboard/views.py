from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    context = {'test_word': "hello_world"}
    return render(request, "main/dashboard.html",context)
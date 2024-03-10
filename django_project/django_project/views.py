from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UploadImageForm

def login(request):
    return render(request, "account/login.html")

def logout_views(request):
    logout(request)
    return redirect('/')

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # บันทึกรูปภาพลงในระบบของคุณ และให้ผู้ใช้ถือกำเนิด
            # ต่อไปทำขั้นตอนนี้ตามที่คุณต้องการ
            # ตัวอย่าง:
            # uploaded_image = form.cleaned_data['image']
            # handle_uploaded_image(uploaded_image)
            return render(request, 'upload_success.html')
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})

@login_required
def dashboard(request):
    context = {'test_word': "hello_world"}
    return render(request, "main/dashboard.html",context)

@login_required
def profile(request):
    return render(request, "main/profile.html")

@login_required
def profile(request):

    return render(request, "main/profile.html")



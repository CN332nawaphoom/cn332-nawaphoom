from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TaskForm, Task
from . import Factory


# Create your views here.
@login_required
def dashboard(request):
    tasks = Task.objects.all()

    context = {'tasks': tasks}
    return render(request, "main/dashboard.html", context)


@login_required
def upload_video(request):
    if request.method == 'POST':
        print(request.FILES)
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()

    context = {'form': form}
    return render(request, "main/upload_video.html", context)

def task_info(request, id):
    task = Task.objects.get(id=id)
    task.detect("YOLOV8")

    return render(request, 'main/task_info.html', {'task':task})


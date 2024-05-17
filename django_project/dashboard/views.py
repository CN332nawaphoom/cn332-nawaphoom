from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TaskForm, Task, Task_process
from . import Factory
import json

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

    return render(request, 'main/task_info.html', {'task':task})


def process(request, id):
    task = Task.objects.get(id=id)
    coordinates = []
    if request.method == "POST":
        data = json.loads(request.POST.get("filledCoordinatesLists"))
        
        for box in data:
            coor = []
            print(box)
            for i in range(1,5):
                c = box[f"coordinates{i}"].split(",")
                coor.append((int(c[0]),int(c[1])))
            coordinates.append(coor)
        print(coordinates)
        data = task.detect("YOLOV8",coordinates)
    
        task_process = Task_process.objects.create(task=task)
        task_process.detected_vdo = 'detection/'+task.get_video_name().split("\\")[-1]
        task_process.extra_data = json.dumps(data)
        task_process.save()

    return redirect("dashboard")

def process_info(request, id):
    task = Task.objects.get(id=id)
    process = Task_process.objects.filter(task=task).first()
    vdo_name = process.detected_vdo.url

    return render(request, 'main/process_info.html', {'task':task, 'vdo_path':vdo_name})
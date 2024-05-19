from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import TaskForm, Task, Task_process
from . import Factory
import json
from django.core.files import File
import os
from django.contrib.auth.models import User

# Create your views here.
@login_required
def dashboard(request):
    tasks = Task.objects.all()

    context = {'tasks': tasks}
    return render(request, "main/dashboard.html", context)


@login_required
def upload_video(request):
    if request.method == 'POST':
        user = request.user
        user_from_db = get_object_or_404(User, username=user.username)
        # print(request.FILES)

        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save()
            task.uploaded_by = user_from_db
            task.save()

    else:
        form = TaskForm()

    context = {'form': form}
    return render(request, "main/upload_video.html", context)

def task_info(request, id):
    task = Task.objects.get(id=id)
    print(task.video.url)
    return render(request, 'main/task_info.html', {'task':task})

def delete_task(request, id):
    task = Task.objects.get(id=id)
    Task_process.objects.filter(task=task).delete()
    task.delete()

    return redirect("dashboard")

def process(request, id):
    task = Task.objects.get(id=id)
    coordinates = []
    if request.method == "POST":
        data = json.loads(request.POST.get("Coordinates&model"))
        print(data["model"])

        for box in data["CoordinatesLists"]:
            coor = []
            for i in range(1,5):
                c = box[f"coordinates{i}"].split(",")
                coor.append((int(c[0]),int(c[1])))
            coordinates.append(coor)

        print(coordinates)
        data = task.detect(data["model"],coordinates)
    
        print("wait process")
    
        video_name = os.path.basename(task.get_video_name())
    
        with open('media/detection/' + video_name, 'rb') as f:
          
            my_video_file = File(f,name=video_name)
            # my_video_file.open()
            # task_process.detected_vdo.save(name="result/"+ video_name,content=my_video_file,save=True)
            task_process = Task_process.objects.create(task=task,detected_vdo=my_video_file)
            task_process.extra_data = json.dumps(data)
            task_process.save()
        task.save()
    return redirect("dashboard")

def process_info(request, id):
    task = Task.objects.get(id=id)
    process = Task_process.objects.filter(task=task).order_by('-id').first()

    if process == None:
        return redirect('dashboard')
    vdo_name = process.detected_vdo.url
    data = process.get_data()

    return render(request, 'main/process_info.html', {'task':task, 'process':process, 'data':data})
from django.shortcuts import render,redirect
from django.urls import reverse
from . import models
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def hello(request):
    return render(request,'task_app/main.html')

@login_required 
def list_task(request):
    all_tasks = models.Task.objects.filter(manager=request.user)
    context = {
        'all_tasks' : all_tasks
    }
    return render(request,'task_app/list_task.html',context=context)

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.manager = request.user
            task.save()
            return redirect(reverse('task_app:list_task'))

    else:
        form = TaskForm()
    return render(request,'task_app/add_task.html',context={'form':form})

@login_required
def update_task(request,pk):
    task = models.Task.objects.get(pk=pk) 
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect(reverse('task_app:list_task'))

    return render(request,'task_app/update_task.html',context={'task':task,'form':form})

@login_required
def delete_task(request,pk):
    task = models.Task.objects.get(pk=pk) 
    task.delete()

    return redirect(reverse('task_app:list_task'))

@login_required
def searchbar(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        tasks = models.Task.objects.filter(Q(title__contains=searched)|Q(description__contains=searched))
        return render(request,'task_app/searchbar.html',context={'searched':searched,'tasks':tasks})
    else:
        return render(request,'task_app/searchbar.html')
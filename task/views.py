from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


# Create your views here.


@login_required
def task_view(request):
    # tasks = Task.objects.raw()
    tasks = Task.objects.all()


    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'home.html', context)


@login_required
def updateView(request, pk):
    tasks = Task.objects.get(id=pk)

    form = TaskForm(instance=tasks)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'update.html', context)


@login_required
def deleteView(request, pk):
    tasks = Task.objects.get(id=pk)

    form = TaskForm()

    if request.method == 'POST':
        tasks.delete()
        return redirect('/')

    context = {'form': form, 'tasks': tasks}
    return render(request, 'deleteTask.html', context)

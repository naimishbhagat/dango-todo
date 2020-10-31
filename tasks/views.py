from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    lists = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'list.html', {'tasks': lists, 'form': form})


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'update_task.html', {'task': task, 'form': form})


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'delete.html', {'item': item})

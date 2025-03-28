from django.shortcuts import render, redirect
from . import forms
from .models import TaskModel

# Create your views here.
def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})

def add_tasks(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_tasks.html', {'form': task_form})

def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)

    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')

    return render(request, 'add_tasks.html', {'form': task_form})

def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('show_tasks')

def complete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')

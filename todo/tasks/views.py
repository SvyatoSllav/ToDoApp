from django.shortcuts import (
    get_object_or_404,
    redirect,
    render
)

from .forms import TaskForm, UpdateTaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'tasks/list.html', context=context)


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = True
    task.save()
    return redirect('/')


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = UpdateTaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form,
        'task': task
    }
    return render(request, 'tasks/update_task.html', context=context)


def delete_task(request, pk):
    get_object_or_404(Task, pk=pk).delete()
    return redirect('/')

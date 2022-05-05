from django.shortcuts import (get_object_or_404, redirect,
                              render)

from .forms import TaskForm, UpdateTaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    form = TaskForm
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        form = TaskForm(request.POST)
        if form.is_valid():
            print(task_title)
            form.save()
        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form
    }

    return render(request, 'tasks/list.html', context=context)


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
    item = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {
        'item': item,
    }
    return render(request, 'tasks/delete.html', context=context)

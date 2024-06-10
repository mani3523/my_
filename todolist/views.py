from django.shortcuts import render, redirect
from todolist.models import Todolist
from todolist.forms import Taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url="/account/login")
@login_required(login_url="/account/login")
def todolist(request):
    all_tasks = Todolist.objects.filter(manager=request.user).order_by('id')
    paginator = Paginator(all_tasks, 5)
    page = request.GET.get('pg')
    all_tasks = paginator.get_page(page)

    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data.get('task', '').strip()
            if task_name:
                instance = form.save(commit=False)
                instance.manager = request.user
                instance.save()
                messages.success(request, "New task successfully added")
                return redirect('todolist')
            else:
                messages.error(request, "Task cannot be empty")
    else:
        form = Taskform()
        
    return render(request, 'todo.html', {'all_tasks': all_tasks, 'form': form})

@login_required(login_url="/account/login")
def features(request):
    context = {
        'todo_features':'Welcome to Taskmate Features page',
    }
    return render(request, 'features.html', context)

def about(request):
    context = {
        'todo_about':'Welcome to Taskmate About us page',
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'todo_contact':'Welcome to Taskmate Contact us page',
    }
    return render(request, 'contact.html', context)

@login_required(login_url="/account/login")
def delete(request, task_id):
    task = Todolist.objects.get(pk=task_id)
    if task.manager == request.user:
        task.delete()
    else:
        messages.error(request, "Access denied! You are not able to delete this task")
    return redirect('todolist')

@login_required(login_url="/account/login")
def edit(request, task_id):
    if request.method == 'POST':
        task = Todolist.objects.get(pk=task_id)
        form = Taskform(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todolist')  
    else:
        task_obj = Todolist.objects.get(pk=task_id)
    return render(request, 'edit.html', {'task_obj': task_obj})

@login_required(login_url="/account/login")
def complete(request, task_id):
    task = Todolist.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, "Access denied! You are not allowed to access this page anymore")
    return redirect('todolist')

@login_required    
def pending(request, task_id):
    task = Todolist.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, "Access denied! You are not able to do this task")
    return redirect('todolist')

def index(request):
    context = {
        'todo_index': 'Welcome to Todolist',
    }
    return render(request, 'index.html', context)


def session(request):
    context = {
        'session': 'session expired',
    }
    return render(request, 'session.html', context)
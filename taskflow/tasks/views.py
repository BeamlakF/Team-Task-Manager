from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, Comment
from .forms import TaskForm
from django.utils import timezone
from django.contrib import messages

def home(request):
    return render(request, 'tasks/home.html')


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments = task.comments.all().order_by('-created_at')

    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(task=task, author=request.user, text=text)
            messages.success(request, 'Comment added!')
            return redirect('task_detail', pk=pk)

    return render(request, 'tasks/task_detail.html', {'task': task, 'comments': comments})


@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        assigned_to_id = request.POST.get('assigned_to')

        if title and assigned_to_id:
            Task.objects.create(
                title=title,
                description=description,
                due_date=due_date or None,
                assigned_to_id=assigned_to_id,
            )
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')

    from .models import CustomUser
    users = CustomUser.objects.all()
    return render(request, 'tasks/task_form.html', {'users': users})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.is_completed = 'is_completed' in request.POST
        task.save()
        messages.success(request, 'Task updated!')
        return redirect('task_detail', pk=task.pk)
    return render(request, 'tasks/task_form.html', {'task': task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted.')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


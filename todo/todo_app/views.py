from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")  # ページをリロードして新しいタスクを表示
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, "todo_app/task_list.html", {"tasks": tasks, "form": form})

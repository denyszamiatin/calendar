from django.shortcuts import render, redirect, get_object_or_404
from .models import Date, Task
from .forms import DateForm, TaskForm


def index(request):
    dates = Date.objects.order_by('dt').all()
    form = DateForm()
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            date = Date(dt=form.cleaned_data['dt'])
            date.save()
            return redirect('/')
    return render(request, 'index.html', {'dates': dates, 'form': form})
    

def get_tasks(request, date_id):
    tasks = Task.objects.filter(dt=date_id)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            date = Task(dt=get_object_or_404(Date, pk=date_id), task=form.cleaned_data['task'])
            date.save()
            return redirect('/date/' + str(date_id))
    return render(request, 'tasks.html', {'tasks': tasks, 'form': form})


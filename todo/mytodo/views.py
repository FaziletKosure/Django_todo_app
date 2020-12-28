from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Todo

from .forms import TodoAddForm

# Create your views here.


def createTodo(request):
    todos = Todo.objects.all()
    form = TodoAddForm()

    if request.method == 'POST':
        form = TodoAddForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('list')

    context = {
        'todos': todos,
        'form': form
    }
    return render(request, 'mytodo/list.html', context)


# Update Todo
def updateTodo(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoAddForm(instance=todo)

    if request.method == 'POST':
        form = TodoAddForm(request.POST, instance=todo)
        if form.is_valid:
            form.save()
        return redirect('list')
    context = {
        'form': form
    }
    return render(request, 'mytodo/update_todo.html', context)

#  Delete Todo


def deleteTodo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('list')

    context = {
        'todo': todo

    }
    return render(request, 'mytodo/delete_todo.html', context)

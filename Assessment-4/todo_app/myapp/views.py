from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from .forms import TodoForm
# Create your views here.


def index(request):
	list=Todo.objects.all()
	return render(request,'index.html',{'list':list})

def add(request):
    list=Todo.objects.order_by("date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = TodoForm()
    return render(request,'add.html',{'form':form,'list':list})


def update(request,id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect ('index')
    form = TodoForm()
    return render(request, 'update.html', {"form":form,"todo":todo})


def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect("index")
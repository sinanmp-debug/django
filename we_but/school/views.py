from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm

def welcome(request):
    return render(request, 'welcome.html')

def upload(request):
    return render(request, 'upload.html')

def task_create_or_update(request,id=None):
    if id:
        task=Task.objects.get(id=id)
    else:
        task=Task()
    if request.method == 'POST':
        form = TAskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
    else:
        form= TaskForm(instance=task)
    return render(request,'task_form.html',{'form':form})
def task_delete(requst,id):
    task = Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('task_list')
    return render(request,'task_confirm_delete.html',{'task':task})
def task_list(request):
    tasks=Task_objects.all()
    return render (request,'task_list.html',{'tasks':tasks})
    
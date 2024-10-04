from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from .forms import TaskForm

# def view_all_tasks(request):
#     tasks = Task.objects.all()
#     return render(request,'task_list.html',{'tasks':tasks}) 

# def add_task(request):
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('view_all_tasks')
#     else:
#         form = TaskForm()     
#     return render(request,'task_form.html',{'form':form})    

# def edit_task(request, task_id):
#     task = get_object_or_404(Task,id=task_id)
#     if request.method == "POST":
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('view_all_tasks')
#     else:
#         form = TaskForm(instance=task)
#     return render(request,'task_form.html',{'form':form})

# def delete_task(request,task_id):
#     task = get_object_or_404(Task, id=task_id)
#     task.delete()
#     return redirect('view_all_tasks')

def task_page(request):
    tasks = Task.objects.all()
    return render(request,'task_page.html',{'tasks':tasks})

def task_add(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        status = request.POST['status']
        
        Task.objects.create(title=title,description=description,priority=priority,status=status)
        messages.success(request,'Add Successfully')
        return redirect('task_page')
    
    else:
        return render(request,'task_add.html')

def edit_taskid(request,id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        status = request.POST['status']

        task.title = title
        task.description = description
        task.priority = priority
        task.status = status

        task.save()
        messages.success(request,"update successfully")
        return redirect('task_page')
    else:
        return render(request,'edit_taskid.html',{'task':task})
    
def delete_taskid(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request,"Delete Successfully")
    return redirect('task_page')

def filter_tasks_by_priority(request):
    if request.method == 'POST':
        priority = request.POST.get('priority')  # Get the priority value from the form (POST data)

        if priority:
            tasks = Task.objects.filter(priority=priority)  # Filter tasks by the selected priority
        else:
            tasks = Task.objects.all()  # If no priority is selected, return all tasks

        return render(request, 'priority.html', {'tasks': tasks, 'selected_priority': priority})
    
    return render(request, 'task_page.html')
from django.urls import path
from taskapp import views

urlpatterns = [
    # path('task1/',views.view_all_tasks,name='view_all_tasks'),
    # path('add_task/',views.add_task,name='add_task'),
    # path('edit_task/<int:task_id>/',views.edit_task,name='edit_task'),
    # path('delete_task/<int:task_id>/',views.delete_task,name='delete_task'),

    path('',views.task_page,name='task_page'),
    path('task_add/',views.task_add,name='task_add'),
    path('edit_taskid/<int:id>/',views.edit_taskid,name='edit_taskid'),
    path('delete_taskid/<int:id>/',views.delete_taskid,name='delete_taskid'),
    path('filter_tasks_by_priority',views.filter_tasks_by_priority,name='filter_tasks_by_priority'),
    
]
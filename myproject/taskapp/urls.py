from django.urls import path
from taskapp import views

urlpatterns = [
    path('',views.view_all_tasks,name='view_all_tasks'),
    path('add_task/',views.add_task,name='add_task'),
    path('edit_task/<int:task_id>/',views.edit_task,name='edit_task'),
    path('delete_task/<int:task_id>/',views.delete_task,name='delete_task'),
    path('task1/',views.task1,name="task1"),
]
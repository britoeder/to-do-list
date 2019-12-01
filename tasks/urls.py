from django.urls import path
from .import views
urlpatterns = [
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('newTask/', views.newTask, name='newTask'),
    path('edit/<int:id>', views.editTask, name='edit-task'),
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
]

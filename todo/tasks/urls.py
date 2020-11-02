from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
    path('api/', views.apiOverview, name='api'),
    path('api/task-list/', views.taskList, name='task-list'),
    path('api/task-create/', views.taskCreate, name='task-create'),
    path('api/task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('api/task-delete/<str:pk>/', views.taskDelete, name='task-delete')
]

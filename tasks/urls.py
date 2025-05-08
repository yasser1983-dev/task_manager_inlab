from django.urls import path
from .views import TaskCreateUpdateView, TaskListDeleteView

urlpatterns = [
    path('projects/<int:project_id>/tasks/create/', TaskCreateUpdateView.as_view(), name='task_create'),
    path('projects/<int:project_id>/tasks/<int:task_id>/edit/', TaskCreateUpdateView.as_view(), name='task_edit'),
    path('project/<int:project_id>/list', TaskListDeleteView.as_view(), name='task_list'),
]
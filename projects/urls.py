from django.urls import path
from .views import ProjectListCreateView, ProjectDeleteView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project_list'),
    path('projects/create/', ProjectListCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
]
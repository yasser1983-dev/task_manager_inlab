from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import get_object_or_404

class ProjectService:
    def __init__(self, user):
        self.user = user

    def list(self):
        return Project.objects.filter(owner=self.user)

    def create(self, data):
        serializer = ProjectSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.save(owner=self.user)

    def delete(self, pk: int):
        project = get_object_or_404(Project, pk=pk, owner=self.user)
        project.delete()
        return project

    def get_project(self, pk: int):
        return get_object_or_404(Project, pk=pk, owner=self.user)
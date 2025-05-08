from projects.models import Project
from .models import Task

class TaskService:
    def __init__(self, user):
        self.user = user

    def create(self, project, data):
        task = Task(**data)
        task.project = project
        task.save()
        return task

    def get_tasks(self):
        return Task.objects.filter(project__owner=self.user)

    def update(self, task_id, data):
        task = Task.objects.select_related('project').get(id=task_id, project__owner=self.user)
        for key, value in data.items():
            setattr(task, key, value)
        task.save()
        return task

    def get_task(self, task_id):
        return Task.objects.select_related('project').get(id=task_id, project__owner=self.user)

    def list_by_project(self, project_id):
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return None
        return Task.objects.filter(project=project)

    def get_tasks_for_user(self):
        return Task.objects.filter(assigned_to=self.user)

    def count_by_status(self, status):
        return Task.objects.filter(assigned_to=self.user, status=status).count()

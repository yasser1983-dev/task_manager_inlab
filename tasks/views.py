from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from django.shortcuts import get_object_or_404, redirect
from .models import Project, Task
from .services import TaskService
from .forms_factory import get_task_form  # factory que retorna TaskForm
from rest_framework import status


class TaskListDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def __init__(self, service_class=None, **kwargs):
        super().__init__(**kwargs)
        self.service_class = service_class or TaskService

    def get(self, request, project_id):
        service = self.service_class(user=request.user)
        tasks = service.list_by_project(project_id=project_id)

        if tasks is None:
            return Response({'detail': 'Proyecto no encontrado o no autorizado'}, status=status.HTTP_404_NOT_FOUND)

        if request.accepted_renderer.format == 'html':
            return Response({'tasks': tasks, 'project_id': project_id}, template_name='tasks/task_list.html')

        return Response({'tasks': [task.to_dict() for task in tasks]}, status=status.HTTP_200_OK)

    def post(self, request, pk):
        return self._delete_logic(request, pk)

    def delete(self, request, pk):
        return self._delete_logic(request, pk)

    def _delete_logic(self, request, pk):
        service = self.service_class(user=request.user)
        task = service.get_task(pk)
        if not task:
            return Response({'detail': 'Tarea no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        service.delete(pk)

        if request.accepted_renderer.format == 'html':
            return redirect('task_list')
        return Response({'detail': 'Tarea eliminada'}, status=status.HTTP_204_NO_CONTENT)

class TaskCreateUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def __init__(self, service_class=None, form_factory=None, **kwargs):
        super().__init__(**kwargs)
        self.service_class = service_class or TaskService
        self.form_factory = form_factory or get_task_form

    def get(self, request, project_id, task_id=None):
        project = get_object_or_404(Project, id=project_id, owner=request.user)

        if task_id:
            task = get_object_or_404(Task, id=task_id, project=project)
            form = self.form_factory(instance=task)
        else:
            form = self.form_factory()

        return Response(
            {'form': form, 'project': project},
            template_name='tasks/task_form.html'
        )

    def post(self, request, project_id, task_id=None):
        project = get_object_or_404(Project, id=project_id, owner=request.user)

        if task_id:
            task = get_object_or_404(Task, id=task_id, project=project)
            form = self.form_factory(request.POST, instance=task)
        else:
            form = self.form_factory(request.POST)

        if form.is_valid():
            service = self.service_class(user=request.user)
            if task_id:
                service.update(task_id=task.id, data=form.cleaned_data)
            else:
                service.create(project=project, data=form.cleaned_data)

            if request.accepted_renderer.format == 'html':
                return redirect('project_list')
            return Response({'success': True}, status=201)

        return Response(
            {'form': form, 'project': project},
            template_name='tasks/task_form.html',
            status=400
        )
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from tasks.services import TaskService
from rest_framework import status


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def __init__(self, service_class=None, **kwargs):
        super().__init__(**kwargs)
        self.service_class = service_class or TaskService

    def get(self, request):
        service = self.service_class(user=request.user)
        tasks = service.get_tasks_for_user()
        counts = {
            'todo': service.count_by_status('todo'),
            'in_progress': service.count_by_status('in_progress'),
            'done': service.count_by_status('done'),
        }

        if request.accepted_renderer.format == 'html':
            return Response({'counts': counts, 'tasks': tasks}, template_name='dashboard/dashboard.html')

        return Response({
            'counts': counts,
            'tasks': [task.to_dict() for task in tasks]
        }, status=status.HTTP_200_OK)

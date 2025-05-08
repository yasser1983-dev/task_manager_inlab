from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer

from .forms_factory import get_project_form
from .services import ProjectService


class ProjectListCreateView(LoginRequiredMixin, APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def __init__(self, service_class=None, form_factory=None, **kwargs):
        super().__init__(**kwargs)
        self.service_class = service_class or ProjectService
        self.form_factory = form_factory or get_project_form

    def get(self, request):
        if request.accepted_renderer.format == 'html':
            if 'create' in request.path:
                # Render template para crear
                form = self.form_factory(request)
                return Response({'form': form}, template_name='projects/project_form.html')
            else:
                # Render template para listar
                service = self.service_class(user=request.user)
                projects = service.list()
                return Response({'projects': projects}, template_name='projects/project_list.html')

        # API GET
        service = self.service_class(user=request.user)
        projects = service.list()
        data = [{'id': p.id, 'name': p.name} for p in projects]
        return Response(data)

    def post(self, request):
        form = self.form_factory(request)
        if form.is_valid():
            service = self.service_class(user=request.user)
            service.create(form.cleaned_data)
            if request.accepted_renderer.format == 'html':
                return redirect('project_list')
            return Response({'success': True}, status=status.HTTP_201_CREATED)

        if request.accepted_renderer.format == 'html':
            return Response({'form': form}, template_name='projects/project_form.html', status=400)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



class ProjectDeleteView(LoginRequiredMixin, APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def __init__(self, service_class=None, **kwargs):
        super().__init__(**kwargs)
        self.service_class = service_class or ProjectService

    def post(self, request, pk):  # Simulación DELETE desde formulario
        return self._delete_logic(request, pk)

    def delete(self, request, pk):  # DELETE real desde cliente API
        return self._delete_logic(request, pk)

    def get(self, request, pk):  # Confirmación antes de eliminar (solo HTML)
        if request.accepted_renderer.format == 'html':
            service = self.service_class(user=request.user)
            project = service.get_project(pk)
            return Response({'project_id': pk, 'project': project}, template_name='projects/project_confirm_delete.html')
        return Response({'detail': 'GET method not allowed for API'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def _delete_logic(self, request, pk):
        service = self.service_class(user=request.user)
        service.delete(pk)

        if request.accepted_renderer.format == 'html':
            return redirect('project_list')
        return Response(status=status.HTTP_204_NO_CONTENT)

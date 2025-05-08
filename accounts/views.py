from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms_factory import get_authentication_form, get_register_form


@method_decorator(csrf_exempt, name='dispatch')
class CustomLoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'accounts/login.html'

    def __init__(self, authentication_form_factory=None, **kwargs):
        super().__init__(**kwargs)
        self.authentication_form_factory = authentication_form_factory or get_authentication_form

    def get(self, request):
        form = self.authentication_form_factory()
        return Response({'form': form}, template_name=self.template_name)

    def post(self, request):
        form = self.authentication_form_factory(request)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.accepted_renderer.format == 'html':
                return redirect('dashboard')
            return Response({'success': True, 'username': user.username})
        return Response({'form': form}, template_name=self.template_name, status=400)

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/register.html'

    def get(self, request):
        form = get_register_form()
        return Response({'form': form})

    def post(self, request):
        form = get_register_form(request)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return Response({'form': form}, status=400)

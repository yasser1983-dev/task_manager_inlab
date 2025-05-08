from .forms import ProjectForm
from .serializers import ProjectSerializer


def get_project_form(request):
    return ProjectForm(request.POST)  if request and request.method == 'POST' else ProjectForm()

def get_project_serializer(data=None, instance=None, partial=False):
    return ProjectSerializer(instance=instance, data=data, partial=partial)

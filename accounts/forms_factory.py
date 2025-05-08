from accounts.forms import CustomAuthenticationForm

from .forms import RegisterForm

def get_register_form(request=None):
    return RegisterForm(request.POST) if request and request.method == 'POST' else RegisterForm()


def get_authentication_form(request=None):
    return CustomAuthenticationForm(
        data=request.POST) if request and request.method == 'POST' else CustomAuthenticationForm()

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from accounts.validators import CustomPasswordValidator


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': _("El campo es requerido."),
        }
    )
    email = forms.EmailField(
        required=True,
        label="Correo electrónico",
        widget=forms.EmailInput(),
        error_messages={
            'invalid': _("Ingresa un correo electrónico válido."),
            'required': _("El correo electrónico es obligatorio."),
        }
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        validators=[CustomPasswordValidator()],
        error_messages={
            'required': _("El campo es requerido."),
        }
    )
    password2 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        validators=[CustomPasswordValidator()],
        error_messages={
            'required': _("El campo es requerido."),
        }
    )
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise ValidationError(_("El nombre de usuario es obligatorio."))
        if User.objects.filter(username=username).exists():
            raise ValidationError(_("Este nombre de usuario ya está en uso."))
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError(_("Este correo ya está registrado."))
        return email

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Por favor, introduce un nombre de usuario y una contraseña correctos. "
            "Ten en cuenta que ambos campos pueden ser sensibles a mayúsculas y minúsculas."
        ),
        'inactive': _("Esta cuenta está inactiva."),
    }
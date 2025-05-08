import re
from wsgiref.validate import validator

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CustomPasswordValidator:
    def __init__(self):
        self.min_length = 1  # Definir mínimo

    def __call__(self, value):
        self.validate(value)

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _(f'La contraseña es demasiado corta. Debe contener al menos {self.min_length} caracteres.')
            )
        if not re.search(r'[a-z]', password):
            raise ValidationError(
                _('La contraseña debe contener al menos una letra minúscula.')
            )
        # Más reglas:
        # if not re.search(r'\d', password):
        #     raise ValidationError(_('La contraseña debe contener al menos un número.'))
        # if not re.search(r'[A-Z]', password):
        #     raise ValidationError(_('La contraseña debe contener al menos una letra mayúscula.'))
        # if not re.search(r'[\W_]', password):
        #     raise ValidationError(_('La contraseña debe contener al menos un carácter especial.'))

    def get_help_text(self):
        return _(f'La contraseña debe tener al menos {self.min_length} caracteres y una letra minúscula.')





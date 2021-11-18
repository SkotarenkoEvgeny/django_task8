import re

from django.core.exceptions import ValidationError
from django.db import models


def is_digit(val):
    if re.search(r'[!@$%^&*()_+=<> ,-.  0-9]', val):
        raise ValidationError(
            'Enter only letters', code='not_digit', params={'value': val}
            )


def is_phone(val):
    if not re.search(r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$', val):
        raise ValidationError(
            'Eter only 0-9 digits and +()- symbols', code='not_phone number',
            params={
                'value':
                    val
                }
            )


class Contact(models.Model):
    first_name = models.CharField(max_length=100, validators=[is_digit])
    last_name = models.CharField(max_length=100, validators=[is_digit])
    e_mail = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20, validators=[is_phone])
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}-{self.first_name}-{self.last_name}'

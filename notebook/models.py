from django.db import models

# Create your models here.


class Contact(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    e_mail = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}-{self.first_name}-{self.last_name}'

from django.contrib import admin

from .models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ["e_mail", "last_name", 'created']
    list_filter = ["created"]
    search_fields = ["e_mail", "last_name"]
    ordering = ["created", "last_name"]

from django.urls import path
from . import views

app_name = 'notebook'

urlpatterns = [
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('<slug:pk>/edit/', views.contact_edit,
         name='contact_edit')
    ]

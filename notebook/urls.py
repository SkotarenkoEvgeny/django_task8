from django.urls import path
from . import views

app_name = 'notebook'

urlpatterns = [
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('<int:contact_id>/', views.contact_detail, name='contact_detail')
    ]

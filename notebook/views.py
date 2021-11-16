from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Contact


# Create your views here.
class ContactListView(ListView):

    queryset = Contact.objects.all()
    context_object_name = 'contacts'
    template_name = 'notebook/list.html'
    paginate_by = 15


def contact_detail(request, contact_id):

    contact_detail = get_object_or_404(Contact, id=contact_id)
    return render(request, 'notebook/detail.html')

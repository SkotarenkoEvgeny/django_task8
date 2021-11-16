from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import ListView

from .models import Contact


# Create your views here.
class ContactListView(ListView):

    queryset = Contact.objects.all()
    context_object_name = 'contacts'
    template_name = 'notebook/list.html'
    paginate_by = 15


def contact_edit(request, pk):

    contact = Contact.objects.get(id=int(pk))

    if request.method == 'POST':
        if request.POST.get('add_button') is not None:
            contact.first_name = request.POST['first_name']
            contact.last_name = request.POST['last_name']
            contact.e_mail = request.POST['e_mail']
            contact.phone_number = request.POST['phone_number']
            contact.save()
        return HttpResponseRedirect(reverse('notebook:contact_list'))
    else:
        return render(request, 'notebook/update.html', {
            'contact': contact,
            'created_1': contact.created.isoformat('#', 'minutes'),
            'modified_1': contact.modified.isoformat('#', 'minutes')
            }
                      )


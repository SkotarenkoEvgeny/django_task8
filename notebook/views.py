from django.shortcuts import HttpResponseRedirect, reverse
from django.views.generic import ListView, UpdateView

from .models import Contact


# Create your views here.
class ContactListView(ListView):
    queryset = Contact.objects.all()
    context_object_name = 'contacts'
    template_name = 'notebook/list.html'
    paginate_by = 15


# class ContactEditView(UpdateView):
#     model = Contact
#     # fields = ['first_name', 'last_name', 'e_mail', 'phone_number', 'created']
#     fields = '__all__'
#     template_name = 'notebook/update.html'
#
#
#
#     def get_success_url(self):
#
#         return '%s?status_message=Contact is success updated' % reverse(
#             'notebook:contact_list'
#             )
#
#     def post(self, request, *args, **kwargs):
#
#         if request.POST.get('cancel_button'):
#             return HttpResponseRedirect(
#                 '%s?status_message=Update canceled' %
#                 reverse('notebook:contact_list')
#                 )
#         else:
#             return super().post(request, *args, **kwargs)

def contact_edit(request, pk):
    print(Contact.objects.all())
    contact = Contact.objects.get(id=int(pk))

    return contact

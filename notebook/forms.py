from .models import Contact
from bootstrap_modal_forms.forms import BSModalModelForm


class ContactModelForm(BSModalModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'e_mail', 'phone_number']

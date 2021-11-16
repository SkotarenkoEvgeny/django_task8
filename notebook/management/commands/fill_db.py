from django.core.management.base import BaseCommand

from randomuser import RandomUser

from notebook.models import Contact


class Command(BaseCommand):

    help = 'add 100 random users'

    def handle(self, *args, **options):
        user_list = RandomUser.generate_users(100)
        for item in user_list:
            contact = Contact(
                first_name=item.get_first_name(),
                last_name=item.get_last_name(),
                e_mail=item.get_email(),
                phone_number=item.get_phone()
                )
            contact.save()
        return f'Added {len(user_list)}'\
            f'In db is {len(Contact.objects.all())} contacts.'

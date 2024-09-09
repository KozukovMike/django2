from .models import Logo, Contacts, Media


def base_context(request):
    return {
        'logo': Logo.objects.first(),
        'contacts_list': Contacts.objects.all(),
        'media_list': Media.objects.all(),
    }

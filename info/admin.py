from django.contrib import admin
from .models import Contacts, Media, Logo
from django.utils.safestring import mark_safe


# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['contact_phone', 'contact_image', 'get_img']
    search_fields = ['contact_phone']
    list_per_page = 10
    list_max_show_all = 100
    readonly_fields = ['get_img']

    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.contact_image.url}" width="80px"')

    get_img.short_description = 'Значок'


admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Media)
admin.site.register(Logo)

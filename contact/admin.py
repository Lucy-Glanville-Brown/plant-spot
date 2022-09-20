from django.contrib import admin
from .models import Contact


class ContactFormAdmin(admin.ModelAdmin):
    """ Admin for the contact form """

    list_display = (
        'created_on',
        'name',
        'email',
        'subject',
        'message',
    )

    ordering = ('created_on',)


admin.site.register(Contact, ContactFormAdmin)

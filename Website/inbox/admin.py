from django.contrib import admin

# Register your models here.
from .models import Inbox

# admin.site.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    list_display = ('recepient', 'sender', 'subject', 'content')
    list_filter = ('recepient', 'sender')

admin.site.register(Inbox, InboxAdmin)

from django.contrib import admin

from Twit_app.models import *

class MessageAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("user", "text", "date")

admin.site.register(Message, MessageAdmin)
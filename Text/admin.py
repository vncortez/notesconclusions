from django.contrib import admin

from Text.models import NodeText, Title, TypeOfText

# Register your models here.

admin.site.register(Title)
admin.site.register(TypeOfText)
admin.site.register(NodeText)

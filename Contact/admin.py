from django.contrib.admin import ModelAdmin, register
from .models import Contact


@register(Contact)
class MaterialPersonAdmin(ModelAdmin):
    icon_name = 'place'
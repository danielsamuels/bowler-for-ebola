# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'image')
admin.site.register(Image, ImageAdmin)


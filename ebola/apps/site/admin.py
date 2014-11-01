# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'image')

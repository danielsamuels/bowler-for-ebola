# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Image

from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.admin import AdminImageMixin


@admin.register(Image)
class ImageAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('image_preview', 'processed_preview', 'uuid', 'ip_address', 'timestamp')
    list_display_links = ('image_preview', 'processed_preview', 'uuid')

    def image_preview(self, obj):
        if obj.image:
            img = get_thumbnail(obj.image, '100')
            return '<img src="{}" />'.format(img.url)
        return ''
    image_preview.allow_tags = True
    image_preview.short_description = "image"

    def processed_preview(self, obj):
        if obj.processed:
            img = get_thumbnail(obj.processed, '100')
            return '<img src="{}" />'.format(img.url)
        return ''
    processed_preview.allow_tags = True
    processed_preview.short_description = "processed"

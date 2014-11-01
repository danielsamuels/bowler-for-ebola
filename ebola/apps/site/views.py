from django.views.generic import CreateView, DetailView

from .models import Image


class ImageCreate(CreateView):
    model = Image
    fields = ['image']


class ImageDetail(DetailView):
    model = Image
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

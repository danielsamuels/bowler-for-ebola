from django.views.generic import CreateView, DetailView

from .models import Image

from ipware.ip import get_real_ip


class ImageCreate(CreateView):
    model = Image
    fields = ['image']

    def form_valid(self, form):
        form.instance.ip_address = get_real_ip(self.request) or self.request.META.get('REMOTE_ADDR', None)
        return super(ImageCreate, self).form_valid(form)


class ImageDetail(DetailView):
    model = Image
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

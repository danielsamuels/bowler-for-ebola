from django.views.generic import CreateView, DetailView

from .response import JSONResponse, response_mimetype
from .models import Image

from ipware.ip import get_real_ip


class ImageCreate(CreateView):
    model = Image
    fields = ['image']

    def form_valid(self, form):
        form.instance.ip_address = get_real_ip(self.request) or self.request.META.get('REMOTE_ADDR', None)
        self.object = form.save()

        data = {
            'url': self.object.get_absolute_url()
        }
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=data.json'
        return response


class ImageDetail(DetailView):
    model = Image
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

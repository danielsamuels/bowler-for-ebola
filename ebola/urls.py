"""URL config for ebola project."""

from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views import generic
from django.conf.urls.static import static


urlpatterns = patterns(
    "",

    # Admin URLs.
    url(r"^admin/", include(admin.site.urls)),

    url(r"^", include('ebola.apps.site.urls', namespace="image")),

    # There's no favicon here!
    url(r"^favicon.ico$", generic.RedirectView.as_view(url="/static/img/favicon.ico")),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += patterns(
        "",
        url("^404/$", generic.TemplateView.as_view(template_name="404.html")),
        url("^500/$", generic.TemplateView.as_view(template_name="500.html")),
    )

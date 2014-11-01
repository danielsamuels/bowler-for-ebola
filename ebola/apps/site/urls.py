"""URL config for ebola project."""

from django.conf.urls import patterns, url


import views


urlpatterns = patterns(
    "",

    # Admin URLs.
    url(r"^$", views.ImageCreate.as_view(), name="create"),
    url(r"^(?P<uuid>[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/$", views.ImageDetail.as_view(), name="detail"),
)

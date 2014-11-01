"""URL config for ebola project."""

from django.conf.urls import patterns


import views


urlpatterns = patterns(
    "",

    # Admin URLs.
    (r"^/$", views.ImageCreate.as_view()),
    (r"^/view/(?P<uuid>[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/$", views.ImageDetail.as_view()),
)

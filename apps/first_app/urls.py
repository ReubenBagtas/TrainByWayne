from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^packages$', views.packages),
    url(r'^contact$', views.contact),
    url(r'^testimonials$', views.testimonials),

]
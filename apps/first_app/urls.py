from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), #HomePage should be on localhost:8000 while on Development
    url(r'^about$', views.about), #About Page  routes to /about
    url(r'^packages$', views.packages), #Packages page routes to /packages
    url(r'^contact$', views.contact), #Contact Page routes to /contact
    url(r'^testimonials$', views.testimonials), #Testimonials Page routes to /testimonials

]
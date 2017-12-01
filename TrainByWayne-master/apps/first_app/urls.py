from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^index$', views.index), #HomePage should be on localhost:8000 while on Development
    url(r'^contact$', views.contact), #Contact Page routes to /contact
    url(r'^testimonials$', views.testimonials), #Testimonials Page routes to /testimonials
    url(r'^confirm$', views.confirmpayment), #where we display total and pay button!
    url(r'^pay$', views.pay),
    url(r'^thanks$', views.thanks),
    url(r'^selectpackage$', views.packageselect),
    url(r'^cartreview$', views.cartreview),
    url(r'^meetYourCoach$', views.meetYourCoach),#MeetYourCoach route
    url(r'^packagePricing$', views.packagePricing), #packagePricing Route
    url(r'^thanks$', views.thanks),
    url(r'^addToCart$', views.addToCart),
    # url(r'^clearCart$', views.clearCart),
    url(r'^cart$', views.cart), #Cart route
    url(r'^admin$',views.admin),

]

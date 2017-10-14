# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import stripe
import ast

from django.shortcuts import render, redirect
pub_key=""
secret_key=''

stripe.api_key = secret_key

# Create your views here.

def index(request): #Controller for Home Page
    try:
        request.session["currentUser"]
    except:
        request.session["currentUser"] = "Current User is Saved"

    return render(request, "index.html")

def confirmpayment(request):
    data= {
        'pub_key': pub_key
    }
    return render(request, 'confirm.html', data)


def pay(request):
    print (request.POST ,"&&&&&&&&&&&&&&&&&&&&&&&")
    customer = stripe.Customer.create(email=request.POST['stripeEmail'], source= request.POST['stripeToken'])

    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 1099,
        currency = 'usd',
        description = 'bundle A'
    )
    return redirect('/thanks')

def thanks(request):
    return render(request, "thanks.html")


def about(request): #Controller for About Page
    return render(request, "about.html")

def packages(request): #Controller for Packages Page
    return render(request, "packages.html")

def contact(request): #Controller for Contact Page
    return render(request, "contact.html")

def testimonials(request): #Controller for Testimonials Page
    return render(request, "testimonials.html")



# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import ast

from django.shortcuts import render, redirect
pub_key=""
secret_key=''



# Create your views here.

def index(request): #Controller for Home Page
    try:
        request.session["currentUser"]
    except:
        request.session["currentUser"] = "Current User is Saved"

    return render(request, "index.html")

def confirmpayment(request):
    print(request.POST)
    data={
        'amount': request.POST['amount']
    }
    return render(request, 'confirm.html', data)


def pay(request):

    return redirect('/thanks')

def thanks(request):
    return render(request, "thanks.html")

def packageselect(request):
    return render(request, 'packageselection.html')

def cartreview(request):
    print(request.POST)
    data={
        'price':request.POST['price']
    }
    return render(request, 'cartreview.html', data)

def about(request): #Controller for About Page
    return render(request, "about.html")

def packages(request): #Controller for Packages Page
    return render(request, "packages.html")

def contact(request): #Controller for Contact Page
    return render(request, "contact.html")

def testimonials(request): #Controller for Testimonials Page
    return render(request, "testimonials.html")



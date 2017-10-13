# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request): #Controller for Home Page
    try:
        request.session["currentUser"]
    except:
        request.session["currentUser"] = "Current User is Saved"

    return render(request, "index.html")

def about(request): #Controller for About Page
    return render(request, "about.html")

def packages(request): #Controller for Packages Page
    return render(request, "packages.html")

def contact(request): #Controller for Contact Page
    return render(request, "contact.html")

def testimonials(request): #Controller for Testimonials Page
    return render(request, "testimonials.html")



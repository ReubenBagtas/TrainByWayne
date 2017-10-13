# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    response = "Hello, I am your first request!"
    context = {
        "email": "blog@gmail.com",
        "name": "mike"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def packages(request):
    return render(request, "packages.html")

def contact(request):
    return render(request, "contact.html")

def testimonials(request):
    return render(request, "testimonials.html")



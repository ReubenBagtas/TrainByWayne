# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    response = "Hello, I am your first request!"
    context = {
        "email": "blog@gmail.com",
        "name": "mike"
    }
    return render(request, "index.html", context)

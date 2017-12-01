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
        request.session['cart'] = []
        request.session['paymentTotal'] = 0

    return render(request, "index.html")

def confirmpayment(request):
    print(request.POST)
    data={
        'amount': request.POST['price'],
        'package_type': request.POST['package_type'],
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

def contact(request): #Controller for Contact Page
    return render(request, "contact.html")

def testimonials(request): #Controller for Testimonials Page
    return render(request, "testimonials.html")

def meetYourCoach(request): #Controller for meetYourCoach Page
    return render(request, "meetYourCoach.html")

def packagePricing(request): #Controller for packagePricing Page
    return render(request, "packagePricing.html")


def cart(request): #Controller for cart Page
    try:
        if request.POST['package'] == "3":
            print("3 month")
            return render(request,"cart3.html")
        elif request.POST['package'] == "1":
            print("1 month")
            return render(request, "cart1.html")
        elif request.POST['package'] == "6":
            print("6 month")
            return render(request, "cart6.html")
        else:
            print("no months *******")
            return render(request, "cart.html")
    except:
        print("not working")
        return render(request, "cart.html")

def admin(request):
    return render(request, "admin.html")

def addToCart(request): #controller for adding packages to cart
    print(request.POST)
    if request.POST['package'] == '1':
        request.session['paymentTotal'] += 125
        request.session['cart'].append('1')
    elif request.POST['package'] == '2':
        request.session['paymentTotal'] += 300
        request.session['cart'].append('2')
    elif request.POST['package'] == '3':
        request.session['paymentTotal'] += 500
        request.session['cart'].append('3')
    return redirect("/cart")

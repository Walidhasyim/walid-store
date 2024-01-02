from django.shortcuts import render, HttpResponseRedirect
from .models import *


# Create your views here.
def homeView(req):

    return render(req, 'index.html')


def menuView(req):

    return render(req, 'menu.html', {"books" : Books.objects.all()})


def detailView(req, **kwargs):
    data = Books.objects.filter(judul=kwargs["name"])


    if not kwargs or not data:
        return HttpResponseRedirect("/")
    

    return render(req, "details.html", {"books" : data[0]})
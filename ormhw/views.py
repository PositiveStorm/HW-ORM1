from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Element


def index(request):
    return redirect('catalog')


def show_catalog(request):
    href = request.GET.get('sort')
    if href == 'name':
        phones = Element.objects.order_by('name')
    elif href == 'min_price':
        phones = Element.objects.order_by('price')
    elif href == 'max_price':
        phones = Element.objects.order_by('-price')
    else:
        phones = Element.objects.all()
    template = 'catalog.html'
    context = {'phone': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone_info = Element.objects.filter(slug=f'{slug}')
    template = 'product.html'
    context = {'phones': phone_info}
    return render(request, template, context)
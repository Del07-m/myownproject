from django.shortcuts import render

from . models import *

# Create your views here.
def storePage(request):

    products =  Product.objects.all()



    return render (request, 'ecom/store.html',{'objects': products})
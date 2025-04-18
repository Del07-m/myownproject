from django.shortcuts import render, redirect

from django.contrib.auth import login
from .form import RegistrationForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from . models import *



# Create your views here.
def storePage(request):

    products =  Product.objects.all()



    return render (request, 'ecom/store.html',{'objects': products})

# cart page


def cartPage(request):

    if request.user.is_authenticated:

     customer = request.user.customer

     order, created = Order.objects.get_or_create(customer=customer,complete=False)

     items = order.orderitem_set.all()

    return render(request, "ecom/cart.html",{"items": "items"})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("login")

       





    form = RegistrationForm()
    return render(request, template_name="ecom/signup.html", context={"form":form})
# END OF SIGNUP LOGIC 

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  
        else:
            messages.info(request, 'username OR password is incorrect')
    context = {}       
    return render(request, 'ecom/login.html', context)

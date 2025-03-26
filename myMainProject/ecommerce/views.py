from django.shortcuts import render, redirect

from django.contrib.auth import login
from .form import RegistrationForm
from django.contrib.auth.models import User


from . models import *



# Create your views here.
def storePage(request):

    products =  Product.objects.all()



    return render (request, 'ecom/store.html',{'objects': products})



def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("login")

       

# return redirect('store')  



    form = RegistrationForm()
    return render(request, template_name="ecom/signup.html", context={"form":form})


username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
from django.urls import path
from . import views

urlpatterns = [
    path('',views.storePage,name = 'homepage'),
    path('register',views.register),
    # path('',views.signIn),
    path('login',views.loginPage),
    path('cart',views.cartPage),

]
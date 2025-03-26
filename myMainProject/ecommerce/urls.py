from django.urls import path
from . import views

urlpatterns = [
    path('',views.storePage),
    path('register',views.register),
    # path('',views.signIn),

]
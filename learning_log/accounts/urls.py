#  define URL patterns for accounts here

from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    # registration page
    path('register/', views.register, name='register'),
]
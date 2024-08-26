#  define URL patterns for accounts here

from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    path('',include('django.contrib.auth.urls')),

]
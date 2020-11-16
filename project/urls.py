from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [	
	url(r'^$', responseform, name = 'index'),
	url(r'^thankyou/$', responseform, name = 'covid'),
	

]


from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.serializers import serialize
from django.templatetags.static import static
from .models import *
from django.views.generic import TemplateView
from .forms import * 
from django.conf import settings



def responseform(request):
 #if form is submitted
     if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            myForm.save()

            template = loader.get_template('thankyou.html')

            return HttpResponse(template.render({},request))



     else:
         form = MyForm()

     return render(request, 'index.html', {'form':form});
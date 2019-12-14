from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def contactHome(request):
   template_name = 'User/home_contact.html'
   content = {"users": "123"}
   return render(request,template_name,content)
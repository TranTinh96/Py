from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


from .forms import (ContactHome)


def Home_Page(request):
   my_title = "Hello here ...."
   template_name = "home.html"
   if(request.user.is_authenticated):
      content = {"title": "My Title", "my_list": [1, 2, 3, 4, 5, 6]}
   return render(request, template_name,)

def Contact_Page(request):
   title = "Contact us"
   template_name = "Home/home_contact.html"
   print(request.POST)
   form = ContactHome(request.POST or None)
   if form.is_valid():
      print(form.cleaned_data)
   return render(request,template_name,{'title': title})
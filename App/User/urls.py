from django.urls import path

from .views import (
   contactHome
)


urlpatterns = [
   path("contact/",contactHome),
  
]
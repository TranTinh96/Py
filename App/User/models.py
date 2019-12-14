from django.db import models

# Create your models here.

class contact_Home(models.Model):
   full_name = models.CharField(max_length=255)
   email = models.EmailField()
   content = models.TextField()
   

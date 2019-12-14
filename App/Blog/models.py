from django.db import models

# Create your models here

class BlogPost(models.Model):
   #id_ = models.IntegerField()
   title = models.TextField() 
   #slug = models.SlugField(unique=True) # Hello World -> Hello-World
   content = models.TextField(null=True,blank=True)

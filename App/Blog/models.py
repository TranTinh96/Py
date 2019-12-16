from django.db import models
from django.conf import settings

# Create your models here
User = settings.AUTH_USER_MODEL
class BlogPost(models.Model):
   #id_ = models.IntegerField()
   user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
   title = models.TextField() 
   content = models.TextField(null=True,blank=True)

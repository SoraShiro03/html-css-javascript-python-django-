from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
   caption = models.CharField(max_length=165)
   image = models.ImageField(upload_to='images/')
   date_posted = models.DateTimeField(auto_now=True)
   like_count = models.IntegerField(default=0)
   author =  models.ForeignKey(User, on_delete=models.CASCADE)


   def __str__(self):
      return self.caption






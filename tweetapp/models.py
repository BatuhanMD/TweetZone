from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone   
# Create your models here.

class Tweet(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Username: {self.username}, Tweet: {self.message}"
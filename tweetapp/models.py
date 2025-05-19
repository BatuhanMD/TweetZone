from django.db import models

# Create your models here.

class Tweet(models.Model):
    nickname = models.CharField(max_length=20)
    message = models.CharField(max_length=255)

    def __str__(self):
        return f"Tweet nick:{self.nickname} message: {self.message}"
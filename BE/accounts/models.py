from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class User(AbstractUser):
    
    nickname = models.CharField(max_length=30, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.nickname
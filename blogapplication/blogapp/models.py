from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Bloguser(AbstractUser):
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=225, null=True)


class Blog(models.Model):
    user_id = models.ForeignKey(Bloguser, on_delete=models.CASCADE)
    image = models.FileField()
    Title = models.CharField(max_length=225,)
    Description = models.CharField(max_length=255)

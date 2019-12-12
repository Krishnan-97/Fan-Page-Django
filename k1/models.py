from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Comment(models.Model):
    """ todo todos table in db"""
    name = models.CharField(max_length=255)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
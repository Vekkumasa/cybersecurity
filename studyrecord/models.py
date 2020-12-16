from django.db import models

from django.contrib.auth.models import User
from django_cryptography.fields import encrypt

# Create your models here.

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    passed = models.BooleanField()
    grade = encrypt(models.IntegerField(default=0))
    comments = models.TextField()
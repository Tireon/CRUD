from django.db import models

class Member(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    post = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

from django.db import models

class HealthExpert(models.Model):
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_avaliable = models.BooleanField(default=False)
    last_avaliable_date = models.DateTimeField(null=True)
    display_image = models.ImageField(upload_to='images/')
    date_joined = models.DateTimeField(auto_now_add=True)

class Patient(models.Model):
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True)
    display_image = models.ImageField(upload_to='images/')
    date_joined = models.DateTimeField(auto_now_add=True)

class Staff(models.Model):
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True)
    display_image = models.ImageField(upload_to='images/')
    date_joined = models.DateTimeField(auto_now_add=True)


# Create your models here.

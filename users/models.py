from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class User(AbstractUser):
    
    def __str__(self):
        return f"{self.email}"


class Specialty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Expert(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                related_name="expert")
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=7, choices=GENDER, null=True, blank=True)
    specialty = models.ForeignKey(Specialty, related_name='specialty', on_delete=models.CASCADE, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_avaliable = models.BooleanField(default=False)
    last_avaliable_date = models.DateTimeField(null=True)
    display_image = models.ImageField(upload_to='images/', null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}"

class Patient(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                related_name="patient")
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True)
    display_image = models.ImageField(upload_to='images/', null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}"

class Staff(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                related_name="staff")
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True)
    display_image = models.ImageField(upload_to='images/', null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}"

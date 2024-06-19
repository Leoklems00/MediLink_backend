from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

def __str__(self):
    return self.email


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
                                related_name="expert", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
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
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                related_name="patient", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=7, choices=GENDER, null=True, blank=True)
    last_login = models.DateTimeField(null=True)
    display_image = models.ImageField(upload_to='images/', null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}"

class Staff(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                related_name="staff", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=7, choices=GENDER, null=True, blank=True)
    last_login = models.DateTimeField(null=True)
    display_image = models.ImageField(upload_to='images/', null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}"


class Review(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE,
                                related_name="patient_review")
    details = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient}"

class Case(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE
                                , related_name="patient_case")
    description = models.CharField(max_length=100)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE,
                                 related_name="case_expert")
    successful = models.BooleanField(default=False)
    reviwe = models.ForeignKey(Review, on_delete=models.CASCADE,
                                 related_name="case_review")
    rating = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient}-{self.expert}"

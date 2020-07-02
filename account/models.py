from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Patient(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True)
    profile_pic = models.ImageField(
        default="default_pic.jpg", null=True, blank=True)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=30, null=True)
    register_no = models.CharField(max_length=30, null=True)
    profile_pic = models.ImageField(
        default="default_pic.jpg", null=True, blank=True)

    def __str__(self):
        return self.name


class Nurse(models.Model):

    xp = (
        ('1 year', '1 year'),
        ('2 years', '2 years'),
        ('3+ years', '3+ years')
    )

    work_days = (
        ('Sunday, Monday, Tuesday', 'Sunday, Monday, Tuesday'),
        ('Monday, Tuesday, Wednesday', 'Monday, Tuesday, Wednesday'),
        ('Tuesday, Wednesday, Thrusday', 'Tuesday, Wednesday, Thrusday'),
        ('Friday, Saturday, Sunday', 'Friday, Saturday, Sunday')
    )
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    Qualification = (
        ('B.Sc in Nursing', 'B.Sc in Nursing'),
        ('Diploma in Nursing', 'Diploma in Nursing')
    )
    hospital = models.ForeignKey(
        Hospital, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=30, null=True, choices=Gender)
    fee_per_day = models.IntegerField(null=True)
    experience = models.CharField(max_length=30, null=True, choices=xp)
    working_days = models.CharField(
        max_length=30, null=True, choices=work_days)
    qualification = models.CharField(
        max_length=30, null=True, choices=Qualification)
    profile_pic = models.ImageField(
        default="default_pic.jpg", null=True, blank=True)

    def __str__(self):
        return self.name


class Hire(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, null=True, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, null=True, on_delete=models.CASCADE)
    hire_date = models.CharField(max_length=200, null=True)
    prescribe_pic = models.ImageField(null=True, blank=True)

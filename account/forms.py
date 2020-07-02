from django.forms import ModelForm
from .models import Hospital, Patient, Nurse, Hire
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class AddNurseForm(ModelForm):
    class Meta:
        model = Nurse
        fields = '__all__'


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['user']


class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
        exclude = ['user']


class HireForm(ModelForm):
    class Meta:
        model = Hire
        fields = '__all__'

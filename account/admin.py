from django.contrib import admin

# Register your models here.
from .models import Hospital, Patient, Nurse, Hire

admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Nurse)
admin.site.register(Hire)

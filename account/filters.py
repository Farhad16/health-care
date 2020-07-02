import django_filters

from .models import Hospital, Patient, Nurse


class NurseFilter(django_filters.FilterSet):
    class Meta:
        model = Nurse
        fields = '__all__'
        exclude = ['name', 'address', 'email',
                   'phone', 'qualification', 'phone', 'profile_pic', 'gender']

from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Hospital, Patient, Nurse, Hire
from .forms import AddNurseForm, CreateUserForm, PatientForm, HospitalForm, HireForm
from .filters import NurseFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unathenticated_user, allowed_users
from django.views.generic import CreateView
from django.contrib.auth.models import Group


def dashboard(request):
    return render(request, 'users/dashboard.html')


def register_select(request):
    template = 'users/register_select.html'
    return render(request, template)


@unathenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='hospital')
            user.groups.add(group)
            Hospital.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for '+username)
            return redirect('login')
    context = {'form': form}
    template = 'users/register.html'
    return render(request, template, context)


def patient_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='patient')
            user.groups.add(group)
            Patient.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for '+username)
            return redirect('login')
    context = {'form': form}
    template = 'users/patient_register.html'
    return render(request, template, context)


@unathenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def patient_profile(request):
    patient = request.user.patient
    template = 'users/patient_profile.html'
    context = {'patient': patient}
    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def patient_update(request):
    patient = request.user.patient
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_profile')
    template = 'users/patient_update.html'
    context = {'form': form}
    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['hospital'])
def hospital_dash(request):
    hospital = request.user.hospital
    nurses = request.user.hospital.nurse_set.all()
    total_nurse = nurses.count()
    template = 'users/hospital_dash.html'
    context = {'hospital': hospital,
               'nurses': nurses, 'total_nurse': total_nurse}
    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['hospital'])
def hospital_profile(request):
    hospital = request.user.hospital
    template = 'users/hospital_profile.html'
    context = {'hospital': hospital}
    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['hospital'])
def hospital_update(request):
    hospital = request.user.hospital
    form = HospitalForm(instance=hospital)

    if request.method == 'POST':
        form = HospitalForm(request.POST, request.FILES, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_profile')
    template = 'users/hospital_update.html'
    context = {'form': form}
    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['hospital'])
def nurse_list(request):
    nurses = request.user.hospital.nurse_set.all()
    context = {'nurses': nurses}
    return render(request, 'users/nurse_list.html', context)


def search_nurse(request):
    nurses = Nurse.objects.all()
    myfilter = NurseFilter(request.GET, queryset=nurses)
    nurses = myfilter.qs
    context = {'nurses': nurses, 'myfilter': myfilter}
    template = 'users/search_nurse.html'
    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def nurse_details(request, pk):
    nurse = Nurse.objects.get(id=pk)
    context = {'nurse': nurse}
    template = 'users/nurse_details.html'
    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['hospital'])
def add_nurse(request):
    form = AddNurseForm()
    if request.method == 'POST':
        form = AddNurseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/nurse_list')
    context = {'form': form}
    return render(request, 'users/add_nurse.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['hospital'])
def update_nurse(request, pk):
    nurse = Nurse.objects.get(id=pk)
    form = AddNurseForm(instance=nurse)

    if request.method == 'POST':
        form = AddNurseForm(request.POST, request.FILES, instance=nurse)
        if form.is_valid():
            form.save()
            return redirect('/nurse_list')
    context = {'form': form, 'nurse': nurse}
    return render(request, 'users/update_nurse.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['hospital'])
def view_nurse(request, pk):
    nurse = Nurse.objects.get(id=pk)
    context = {'nurse': nurse}
    template = 'users/view_nurse.html'
    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['hospital'])
def delete_nurse(request, pk):
    nurse = Nurse.objects.get(id=pk)
    if request.method == 'POST':
        nurse.delete()
        return redirect('/nurse_list')
    context = {'nurse': nurse}
    template = 'users/delete_nurse.html'
    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def hire_nurse(request, pk):
    nurse = Nurse.objects.get(id=pk)
    form = HireForm()
    if request.method == 'POST':
        form = HireForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Your Hire is taken place, You will get an confimation sms soon in your phone number')
    context = {'form': form, 'nurse': nurse}
    template = 'users/hire_nurse.html'
    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['hospital'])
def hire_noti(request):
    hires = request.user.hospital.hire_set.all()
    total_hire = hires.count()
    context = {'hires': hires, 'total_hire': total_hire}
    return render(request, 'users/hire_noti.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['hospital'])
def nurse_reserve_details(request, pk):
    hire = Hire.objects.get(id=pk)
    context = {'hire': hire}
    template = 'users/nurse_reserve_details.html'
    return render(request, template, context)

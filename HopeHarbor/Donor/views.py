from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Donor
from .forms import Donor_Login_Form, Donor_Registration_Form
# Create your views here.


def index(request):
    return render(request, 'index.html')




def DiK(request):
    return render(request, 'DIKpage.html')


def donor_entry_request(request):
    if request.method == "POST":
        form = Donor_Login_Form(request.POST)
        if form.is_valid():
            Username = form.cleaned_data.get('Username')
            Password = form.cleaned_data.get('Password')

            condition1 = Donor.objects.filter(Username=Username)
            condition2 = Donor.objects.filter(Password=Password)
            if condition1 and condition2:
                return redirect('donor:index')
            elif condition1 and Password != condition2:
                raise ValidationError("Incorrect Password!")
            else:
                raise ValidationError("No user found!")
    else:
        form = Donor_Login_Form()

    return render(request, 'login.html', {'form' : form})

def registration(request):
    if request.method == 'POST':
        form = Donor_Registration_Form(request.POST)
        if form.is_valid():
            Username = form.cleaned_data.get('Username')

            condition1 = Donor.objects.filter(Username=Username)
            if condition1:
                raise ValidationError("User already exists!")
            else:
                form.save()
                return HttpResponse("Welcome Donor")
    else:
        form = Donor_Registration_Form()

    return render(request, 'registration.html', {'form':form})
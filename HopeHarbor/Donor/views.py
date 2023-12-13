from django.core.exceptions import ValidationError
from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import Donor
from .forms import Donor_Login_Form, Donor_Registration_Form
# Create your views here.


def index(request):
    return render(request, 'index.html')




class DiK(View):
    template='index.html'

    def get(self, request):
        uname = request.session['username']
        return render(request, self.template, {'Username': uname})

    def post(self, request):
        uname = request.session['username']
        request.session['username'] = uname
        return redirect('/goods')


def donor_entry_request(request):
    if request.method == "POST":
        form = Donor_Login_Form(request.POST)
        if form.is_valid():
            Username = form.cleaned_data.get('Username')
            Password = form.cleaned_data.get('Password')

            condition1 = Donor.objects.filter(Username=Username)
            condition2 = Donor.objects.filter(Password=Password)
            if condition1 and condition2:
                request.session['username'] = Username
                return HttpResponseRedirect('/DiK')
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


class InsertGoods(View):
    template = 'DIKpage.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        quantity = request.POST['quantity']
        label = request.POST['label']
        perishable = 'perishable' in request.POST
        expiry = request.POST['expiry']
        cursor = connection.cursor()
        username = request.session['username']
        args = [perishable, expiry or None, label, username, quantity]
        cursor.callproc('InsertGoodsDonation', args)
        result = cursor.fetchall()
        cursor.close()
        print(result)
        msg = request.session['username']
        request.session['username'] = username
        return redirect('/goodstracker')



class displayGoodsTracker(View):
    template = 'DonationTracker.html'

    def get(self, request):
        donor_username = request.session['username']
        cursor = connection.cursor()
        cursor.callproc('DisplayGoodsTracker', [donor_username])
        results = cursor.fetchall()
        cursor.close()
        print(results)
        return render(request, self.template, {'results': results})




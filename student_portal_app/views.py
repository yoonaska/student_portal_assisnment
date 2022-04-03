from django.urls import reverse
from django.views import generic
from unicodedata import name
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import*
from . forms import*
from django.contrib.auth.models import User

# Create your views here.
def login(request):
   if request.user.is_authenticated:
       is_superuser = request.user.is_superuser
       if not is_superuser:
           return redirect("userhome")
       else:
           return redirect("adminhome")
        
   if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request,user)
            is_superuser = request.user.is_superuser
            if not is_superuser:
                return redirect("userhome")
            else:
                return redirect("adminhome")           
        else:
            print("invalid credentials")
   return render(request,"login.html")

   
def logout(reqest):
    auth_logout(reqest)


def userhome(request):
    userId = request.user.id
    return render(request,"userhome.html", {'userId': userId})

def adminhome(request):
    registeredUsers = studentDetails.objects.all()
    return render(request,"adminhome.html", {'data': registeredUsers})

def createuser(request):
    if request.method == 'GET':
        form = studentDetailsForm()
        return render(request, 'createuser.html', {"form":form})
    if request.method =="POST":
        form = studentDetailsForm(request.POST)
        if form.is_valid(): 
            firstname = form.cleaned_data['firstName']
            lastname = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phonenumber']
            address1 = form.cleaned_data['addressOne']
            address2 = form.cleaned_data['addressTwo']   

            
            tempUser = User.objects.create_user(username=email,
                                 email=email,
                                 password=password)  

            profileModel = studentDetails(user=tempUser, email=email, firstName=firstname, lastName=lastname, addressOne=address1, addressTwo = address2, phonenumber=phone)
            profileModel.save()
            return redirect("adminhome")
        else:
            return render(request, "createuser.html")    

def delete_stud(request,pk=None):
    studentDetails.objects.get(id=pk).delete()
    return redirect("adminhome")


def update_stud(request,pk=None):
    stud = studentDetails.objects.get(user=pk)
    return render(request,"editprofile.html", {'data' : stud})
    
        
def update_stud_details(request, pk):
    form = studentDetailsForm(request.POST)
    if form.is_valid(): 
        stud = studentDetails.objects.get(user=pk)

        userValue = User.objects.get(id=pk);
        print(pk)
        print(userValue)
        firstname = form.cleaned_data['firstName']
        lastname = form.cleaned_data['lastName']
        password = form.cleaned_data['password']
        phone = form.cleaned_data['phonenumber']
        address1 = form.cleaned_data['addressOne']
        address2 = form.cleaned_data['addressTwo']  
        stud.firstName = firstname
        stud.lastName = lastname
        stud.phonenumber = phone  
        stud.addressOne = address1
        stud.addressTwo = address2
        stud.save()
        if len(password) > 0:
            userValue.set_password(password)
            userValue.save()            
    return redirect("/")

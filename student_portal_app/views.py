from django.views import generic
from unicodedata import name
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import*
from . forms import*

# Create your views here.
def stud_login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method =="POST":
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
   
        else:
            print("invalid credentials")
    return redirect("login")

   
def stud_logout(reqest):
    if request.user.is_authenticated:
        logout(request)
    return redirect(login)



def home(requst):
    if request.user.is_authenticated:
        return render(request,'home.html')
    
    return redirect("login")


   
#FOR NOTE SECTION
def notes (request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user,title= request.POST['title'],discrption= request.POST['discrption'])
            notes.save()
        messages.success(request,"note is added from{request.user.username} sucessfully")

    else:
        form = NotesForm()
    print(request.user)
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,'form':form}
    return render(request, 'notes.html', context,)   


def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")


class NotesDetaisView(generic.DetailView):
    model = Notes
    template_name = 'notes_detail.html'

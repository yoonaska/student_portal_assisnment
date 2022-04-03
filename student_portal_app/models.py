from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class studentDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.TextField(max_length=200)
    lastName = models.TextField(max_length=200)
    phonenumber = models.TextField(max_length=200,default=None)
    email = models.EmailField(max_length = 254)
    addressOne = models.TextField(max_length=500)
    addressTwo = models.TextField(max_length=500)
    def __str__(self):
        return self.firstName



class sudentRegistration(models.Model):
    name = models.CharField(max_length=150,default=0)
    std = models.CharField(max_length=50,default=0)
    username = models.EmailField(max_length = 254)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    def __str__(self):
        return self.std,self.name
    
    class Meta:
        verbose_name= "sudentRegistration"
        verbose_name_plural= "Create student"


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    discrption = models.TextField(max_length=200)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name= "notes"
        verbose_name_plural= "notes"

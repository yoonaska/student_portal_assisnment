from cgitb import text
from dataclasses import field, fields
from tkinter import Widget
from django import forms
from .models import *
from django.db import models


class NotesForm(forms.ModelForm):
      
      class Meta:
            model = Notes
            fields = ['title','discrption']
class DateInput(forms.DateInput):
      input_type = 'date'
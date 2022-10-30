from tkinter import Widget
from django.core import validators
from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'mobilenumber', 'details']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobilenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.TextInput(attrs={'class': 'form-control'}),


        }

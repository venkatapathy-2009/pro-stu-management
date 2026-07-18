from django import forms
from django.forms import ModelForm
from .models import student


class stu_form(ModelForm):
    class Meta:
        model = student
        fields = "__all__"
        labels = {
            'idi': 'Student ID',
            'name': 'Full name',
            'roll_no': 'Roll number',
            'email': 'Email address',
        }
        widgets = {
            'idi': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Student ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'roll_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Roll number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
        }
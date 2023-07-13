from django import forms
from django.forms import ModelForm
from .models import Student_data


class StudentForm(ModelForm):
    class Meta:
        model = Student_data
        fields = "__all__"
        
widgets = {
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'FirstName'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LastName'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender'}),
            'mobileNumber': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'MobileNumber'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'dob': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'DOB'}),

        }
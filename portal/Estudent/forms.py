from django.forms import ModelForm
from django import forms
from .models import Student_informations

class RegistForm(ModelForm):
    class Meta:
        model = Student_informations
        fields = ["Name", "Father", "GrandFather", "Gender", "MaritalStatus", "MatricResult", "DateOfBirth", "Age", "PlaceOfBirth", "Photo", "Nationality", "Region", "Disability","Email","Phone", "Password"]
        
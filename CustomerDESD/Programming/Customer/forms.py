from django import forms
from Customer.models import User
from Customer.models import Film

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("userName", "password", "name", "dob", "phone", "email", "address",)   # NOTE: the trailing comma is required

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ("title", "ageRating", "description", "duration",)   # NOTE: the trailing comma is required
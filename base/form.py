from dataclasses import field, fields
from distutils.log import error
from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import RL1, RL2, Base, RespoFin, RespoINf, RchA

# class RoleForm(forms.ModelForm):
#     class Meta:
#         model= Roles
#         fields= ['role']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    role = forms.Select()

    class Meta:
        model = Base
        fields = ("email", "role", "password1", "password2")

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label = 'Password', widget=forms.PasswordInput)
    role = forms.Select()


    class Meta :
        model = Base
        fields = ('email', 'role' , 'password')
    def clean(self):
        if self.is_valid():
            email =self.cleaned_data['email']
            role = self.cleaned_data['role']
            password = self.cleaned_data['password']
            if not authenticate(email=email,role=role,  password=password):
                raise forms.ValidationError("invalid")



class Rl1Form(forms.ModelForm):
    
    class Meta:
        model = RL1
        fields = '__all__'
        exclude = ['role']

class Rl2Form(forms.ModelForm):
    
    class Meta:
        model = RL2
        fields = '__all__'
        exclude = ['role']
class ResInf(forms.ModelForm):
    
    class Meta:
        model = RespoINf
        fields = '__all__'
        exclude = ['role']

class ResFin(forms.ModelForm):
    
    class Meta:
        model = RespoFin
        fields = '__all__'
        exclude = ['role']

class ResCa(forms.ModelForm):
    class Meta:
        model = RchA
        fields = '__all__'
        exclude = ['role']
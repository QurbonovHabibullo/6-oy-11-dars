from django import forms
from .models import Turlar,Gullar

class TurForm(forms.Form):
    name = forms.CharField(max_length=100,label ="Tur nomi")
    description = forms.CharField(widget=forms.Textarea,label="Ta'rifi",required=False)
    
    
class GulForm(forms.Form):
    name = forms.CharField(max_length=100,label="Gul nomi")
    description = forms.CharField(widget=forms.Textarea,label="Gul ta'rifi",required=False)
    price = forms.DecimalField(max_digits=10,decimal_places=2,label="narxi")
    turi = forms.ModelChoiceField(queryset=Turlar.objects.all(),label="Tur nomi")
    
    
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password  = forms.CharField(min_length=8,widget=forms.PasswordInput())
    password_repeat  = forms.CharField(min_length=8,widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput())
    password  = forms.CharField(min_length=8,widget=forms.PasswordInput())
    
    
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from App.business.models import models_accion_periodo 


class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    id = forms.IntegerField()
    password1 = forms.CharField(label= 'Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Re Pass', widget=forms.PasswordInput)

    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}

class accion_periodo(forms.ModelForm):

    desde = forms.DateField()
    empresa = forms.CharField()
    accion = forms.CharField()

    class Meta:
        model = models_accion_periodo
        fields = ['desde', 'empresa', 'accion']
    
   
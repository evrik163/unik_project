from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'password')
        wdgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'password1': forms.PasswordInput(attrs={'class': "form-control"}),
            }


class CustomRegForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label='Повтор пароля',
                               widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
       model = User
       fields = ('username', 'password1', 'password2')
       widgets = {
          'username' : forms.TextInput(attrs = {'class' : 'form-control'}),
          'password1' : forms.PasswordInput(attrs = {'class' : 'form-control'}), 
          'password2' : forms.PasswordInput(attrs = {'class' : 'form-control'}),
      }


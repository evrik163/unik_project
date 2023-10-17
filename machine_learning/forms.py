from django import forms
from .models import FinalRes 

class ResultsForm(forms.Form):
    battery_power = forms.DecimalField(label='Введите мощность батареи в мАч',
                                   widget=forms.TextInput(attrs={'class': "form-control"}))
    int_memory = forms.CharField(label='Введите количество единиц памяти(ПЗУ ГБ)',
                                widget=forms.TextInput(attrs={'class': "form-control"}))
    mobile_wt = forms.CharField(label='Введите вес телефона(Граммы)',
                                   widget=forms.TextInput(attrs={'class': "form-control"}))

    
    class Meta:
       model = FinalRes
       fields = ('battery_power', 'int_memory', 'mobile_wt')
       widgets = {
          'battery_power' : forms.TextInput(attrs = {'class' : 'form-control'}),
          'int_memory' : forms.PasswordInput(attrs = {'class' : 'form-control'}), 
          'mobile_wt' : forms.PasswordInput(attrs = {'class' : 'form-control'}),
      }


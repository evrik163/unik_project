from django import forms
 

class ResultsForm(forms.Form):
    area = forms.CharField(label='Введите площадь')

from django.shortcuts import render
from django.contrib import messages
from joblib import load

from mysite.forms import CustomRegForm, CustomAuthForm
from .forms import ResultsForm
from .models import FinalRes
from .train import start_train


TEMPLATE='machine_learning/learn.html'
forms = {"auth_form": CustomAuthForm(), "reg_form": CustomRegForm(),
        'res_form': ResultsForm()}


def homere(request):
    form = ResultsForm(request.POST)

    if form.is_valid():
        clean = {'battery_power': int(form.cleaned_data.get('battery_power')),
                 'int_memory': int(form.cleaned_data.get('int_memory')),
                 'mobile_wt': int(form.cleaned_data.get('mobile_wt'))
                 }
        lst = [obj for obj in clean.values()]
        model = load('machine_learning/final.joblib')
        clean['category'] = int(model.predict(lst))
        FinalRes(**clean).save()
        return render(request, TEMPLATE, {'res': f'{clean["category"]} тип категории',
                                          **forms})
    return render(request, TEMPLATE, forms)


def retrain(request):
    start_train()
    messages.success(request, 'Модель была переобучена')
    return render(request, TEMPLATE, forms)


def show(request):
    results = FinalRes.objects.all()
    return render(request, 'machine_learning/show.html', {'res': results,
                                                         **forms})

from django.shortcuts import render
from joblib import load

from mysite.forms import CustomRegForm, CustomAuthForm
from .forms import ResultsForm
from .models import Results

TEMPLATE='machine_learning/learn.html'
forms = {"auth_form": CustomAuthForm(), "reg_form": CustomRegForm(),
        'res_form': ResultsForm()}


def homere(request):
    form = ResultsForm(request.POST)

    if form.is_valid():
        f_1 = int(form.cleaned_data.get('area'))
        model = load('machine_learning/model_1.joblib')
        result = int(model.predict([[f_1]])[0])
        Results(area=f_1, price=result).save()
        return render(request, TEMPLATE, {'res': f'{result} RUB',
                                       **forms})
    return render(request, TEMPLATE, forms)

def show(request):
    results = Results.objects.all()
    print(results)
    return render(request, 'machine_learning/show.html', {'res': results,
                                                         **forms})

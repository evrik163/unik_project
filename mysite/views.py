from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View

from .models import Post
from .translate import translate
from .forms import CustomRegForm, CustomAuthForm

auth_form = CustomAuthForm() 
reg_form = CustomRegForm()
forms = {"auth_form": auth_form, "reg_form": reg_form}
TEMPLATE = 'mysite/new.html'


def blog_send(request):
    return render(request, 'mysite/blog.html', forms)


def paging(request):
    lst = Post.objects.get_queryset().order_by('id')
    paginator = Paginator(lst, 3)
    page_number  = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'mysite/pag.html', {**forms, 'page_obj': page_obj, 'lst':page_obj})


def test(request):
    lang = request.GET.get('lang')
    string = request.GET.get('string')
    if string:
        res = translate(string, lang)
        return render(request, 'mysite/trans.html', {**forms, 'res': res})
    return render(request, 'mysite/trans.html', forms)


class LoginUser(LoginView):
   template_name = TEMPLATE

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'reg': reverse_lazy('register'),
                        'hi': 'some',
                        **forms})
        return context

   def get_success_url(self):
        return reverse_lazy('workflow')


class Register(View):

    def get(self, request):
        form = CustomRegForm()
        return render(request, TEMPLATE, {'form': form})

    def post(self, request):
        form = CustomRegForm(request.POST)
        print(form.is_valid())

        if form.is_valid():
            form.save()
            return redirect('/')

        return render(request, TEMPLATE, forms)

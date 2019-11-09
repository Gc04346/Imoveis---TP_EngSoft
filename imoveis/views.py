from django.shortcuts import render, redirect
from .forms import ApartamentoForm, CasaForm


def home(request):
    return render(request, 'home.html')


def casa(request):
    context = dict()
    if request.method == 'POST':
        form = CasaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CasaForm()
        context['form'] = form
    return render(request, 'forms.html')


def apartamento(request):
    context = dict()
    if request.method == 'POST':
        form = ApartamentoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ApartamentoForm()
        context['form'] = form
    return render(request, 'forms.html')

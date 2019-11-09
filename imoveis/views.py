from django.shortcuts import render, redirect
from .forms import ApartamentoForm, CasaForm
from .models import Casa, Apartamento

def home(request):
    return render(request, 'home.html')

#Casa
def casa_create(request):
    context = dict()
    context['tipo'] = 'casas'
    if request.method == 'POST':
        form = CasaForm(request.POST)
        if form.is_valid():
            casa = form.save()
            return redirect('casa_edit', casa.id)
    else:
        form = CasaForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def casa_view(request):
    context = dict()
    context['casas'] = Casa.objects.all()
    context['tipo'] = 'casas'
    return render(request, 'view.html', context=context)

def casa_edit(request, casa_id):
    context = dict()
    casa = Casa.objects.get(id=casa_id)
    context['casa'] = casa
    context['tipo'] = 'casas'
    if request.method == 'POST':
        form = CasaForm(request.POST, instance=casa)
        if form.is_valid():
            form.save()
            return redirect('casa_view')
    else:
        form = CasaForm(initial=model_to_dict(casa))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def casa_delete(request, casa_id):
    context = dict()
    Hotel.objects.delete(id=casa_id)
    context['tipo'] = 'casas'
    return redirect('casa_view')

#Apartamento
def apartamento_create(request):
    context = dict()
    context['tipo'] = 'apartamentos'
    if request.method == 'POST':
        form = ApartamentoForm(request.POST)
        if form.is_valid():
            apartamento = form.save()
            return redirect('apartamento_edit', apartamento.id)
    else:
        form = ApartamentoForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def apartamento_view(request):
    context = dict()
    context['apartamentos'] = Apartamento.objects.all()
    context['tipo'] = 'apartamentos'
    return render(request, 'view.html', context=context)

def apartamento_edit(request, apartamento_id):
    context = dict()
    apartamento = Apartamento.objects.get(id=apartamento_id)
    context['apartamento'] = apartamento
    context['tipo'] = 'apartamentos'
    if request.method == 'POST':
        form = ApartamentoForm(request.POST, instance=apartamento)
        if form.is_valid():
            form.save()
            return redirect('apartamento_view')
    else:
        form = ApartamentoForm(initial=model_to_dict(apartamento))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def apartamento_delete(request, apartamento_id):
    context = dict()
    Hotel.objects.delete(id=apartamento_id)
    context['tipo'] = 'apartamentos'
    return redirect('apartamento_view')

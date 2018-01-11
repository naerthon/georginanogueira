from django.shortcuts import render
from .models import Images, Eventos, Colecoes, Galeria
from .forms import EmailForm
from django.http import HttpResponse, HttpResponseRedirect


def submenu():
    menu = Colecoes.objects.all()
    return menu

def index(request):
    template_name = 'index.html'
    context = dict(submenu=submenu())
    return render(request,template_name,context)

def comocomprar(request):
    template_name = 'comocomprar.html'
    context = dict(submenu=submenu())
    return render(request,template_name,context)

def galeria(request):
    template_name = 'galeria/galeria.html'
    rows = Galeria.objects.all()
    context = dict(submenu=submenu(),rows=rows)
    return render(request,template_name,context)

def eventos(request):
    template_name = 'eventos/eventos.html'
    rows = Eventos.objects.all()
    context = dict(submenu=submenu(),rows=rows)
    return render(request,template_name,context)

def detail_eventos(request,slug):
    template_name = 'eventos/detalhe.html'
    rows = Eventos.objects.get(slug=slug)
    context = dict(submenu=submenu(),rows=rows)
    return render(request,template_name,context)

def detail_colecoes(request,slug):
    template_name = 'colecoes/detalhe.html'
    rows = Colecoes.objects.get(slug=slug)
    context = dict(submenu=submenu(),rows=rows)
    return render(request,template_name,context)

def detail_galeria(request,slug):
    template_name = 'galeria/detalhe.html'
    rows = Galeria.objects.get(slug=slug)
    context = dict(submenu=submenu(),rows=rows)
    return render(request,template_name,context)

def contato(request):
    template_name = 'contato/contato.html'
    forms = EmailForm(request.POST)
    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('/')
    else:
        forms = EmailForm()
    context = dict(submenu=submenu(),forms=forms)
    return render(request,template_name,context)
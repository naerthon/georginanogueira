from django.shortcuts import render
from .models import Images


def index(request):
    template_name = 'index.html'
    rows = Images.objects.all()
    context = dict(rows=rows)
    return render(request,template_name,context)
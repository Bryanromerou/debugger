from django.shortcuts import render
from django.http import HttpResponse
from .models import Bug

def homepage(request):
    return render(request = request,
                  template_name = 'main/home.html',
                  context = {"Bugs": Bug.objects.all()})

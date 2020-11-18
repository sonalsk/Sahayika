from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *


def home(request):
    return render(request, 'main/index.html')


def registerPage(request):
    form = NGOregistrationForm()
    if request.method == 'POST':
        form = NGOregistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'main/registration.html', {'form': form})

def volunteer(request):
    form = VolunteerForm()
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'main/Registeration2.html', {'form': form})

# Create your views here.

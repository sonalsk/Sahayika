from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *


def home(request):
    return render(request, 'main/landingpage.html')


def registerPage(request):
    form = NGOregistrationForm()
    if request.method == 'POST':
        form = NGOregistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'main/register.html', {'form': form})

# Create your views here.

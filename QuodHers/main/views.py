from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main/landingpage.html')

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.contrib import messages

def home(request):
    return render(request, 'main/index.html')

def ngohome(request):
    return render(request, 'main/ngoindex.html')

def loginPage(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'main/login.html', context)




def DummyregisterPage(request):
    form = UserCreationForm()
    context = {'form': form}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'main/DummyRoute.html', context)



def registerPage(request):
    form = NGOregistrationForm()
    if request.method == 'POST':
        form = NGOregistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application sent successfully' , extra_tags='alert')
            return redirect('home')
    return render(request, 'main/registration.html', {'form': form})

def volunteer(request):
    form = VolunteerForm()
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application sent successfully', extra_tags='alert')
            return redirect('home')
    return render(request, 'main/Registeration2.html', {'form': form})




def volunteerMain(request):
    form = VolunteerForm()
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application sent successfully', extra_tags='alert')
            return redirect('home')
    return render(request, 'main/Volunteer.html', {'form': form})


# Create your views here.
def feedbackview(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback :)', extra_tags='alert')
            return redirect('home')
    return render(request, 'main/feedback.html', {'form': form})


def gallery(request):
    Feedback = feedback.objects.all()
    return render(request, 'main/gallery.html', {'Feedback': Feedback})


def listofngos(request):
    Ngo = newNGO.objects.all()
    return render(request, 'main/ngos.html', {'Ngo': Ngo})

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NGOregistrationForm(forms.ModelForm):
    class Meta:
        model = newNGO
        fields = ['NGOname','NgoLogo','website','Location', 'PhoneNumber', 'VerificationImage', 'Cause', 'emailid']


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['FullName', 'CommunityOrInstitution', 'Address', 'PhoneNumber', 'VerificationImage', 'Gender',
                  'WhyDoYouWantToHelp', 'Age', 'emailid']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['image', 'message']

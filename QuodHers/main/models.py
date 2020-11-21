from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class NGO(models.Model):
    NGOname = models.CharField(max_length=200, default='')
    Location = models.CharField(max_length=5000,default='')
    PhoneNumber = models.IntegerField(default=0)
    NgoLogo = models.ImageField(default='', upload_to="../media")
    website = models.CharField(max_length=200, default='')
    emailid = models.EmailField(default='xyz@xyz.com')
    VerificationImage = models.ImageField(default='', upload_to="../media")
    Cause = models.CharField(max_length=5000, default='')

    def __str__(self):
        return self.NGOname


class Volunteer(models.Model):
    FullName = models.CharField(max_length=200, default='')
    emailid = models.EmailField(default='xyz@xyz.com')
    CommunityOrInstitution = models.CharField(max_length=200, default='')
    Address = models.CharField(max_length=5000,default='')
    PhoneNumber = models.IntegerField(default=0)
    Age = models.IntegerField(default=0)

    Gender = models.CharField(max_length=200, default='')
    VerificationImage = models.ImageField(default='', upload_to="../media")
    WhyDoYouWantToHelp = models.CharField(max_length=5000, default='')

    def __str__(self):
        return self.FullName




class feedback(models.Model):
    image = models.ImageField(default='', upload_to="../media")
    message = models.TextField( default='')
    def __str__(self):
        return self.message


class newNGO(models.Model):
    NGOname = models.CharField(max_length=200, default='')
    Location = models.CharField(max_length=5000,default='')
    PhoneNumber = models.IntegerField(default=0)
    NgoLogo = models.ImageField(default='', upload_to="../media")
    website = models.CharField(max_length=200, default='')
    emailid = models.EmailField(default='xyz@xyz.com')
    VerificationImage = models.ImageField(default='', upload_to="../media")
    Cause = models.CharField(max_length=5000, default='')

    def __str__(self):
        return self.NGOname
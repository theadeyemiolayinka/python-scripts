from django import forms 
from django.forms import widgets
from . models import *

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlMap
        fields = ['url', 'urlShorten']
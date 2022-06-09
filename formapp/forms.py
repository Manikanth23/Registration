from django import forms
from .models import Registration
from django.forms import ModelForm

class RegForm(ModelForm):
    class Meta:
        model=Registration
        fields="__all__"

# Jednoduchý formulář pro přidání záznamu
from django import forms
from .models import Software

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'
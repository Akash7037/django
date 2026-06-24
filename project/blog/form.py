from django import forms
from .models import data

class ProductForm(forms.ModelForm):
    class Meta:
        model = data
        fields = ["title","body"] 
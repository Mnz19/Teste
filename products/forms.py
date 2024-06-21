from .models import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nome', 'valor', 'descricao', 'disponivel']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'disponivel': forms.Select(attrs={'class': 'form-control'}),
        }
# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['dia_inicio', 'dia_fim', 'moeda']

        widgets = {
            'dia_inicio': forms.DateInput(attrs={'class': 'data_inicial'}),
            'dia_fim': forms.DateInput(attrs={'class': 'data_final'}),
            'moeda': forms.Select(attrs={'class': 'form-control'}),
        }
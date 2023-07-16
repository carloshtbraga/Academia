from django import forms
from .models import Academia


class Formulario(forms.ModelForm):
    class Meta:
        model = Academia
        fields = ["nome", "endereco", "telefone", "foto"]

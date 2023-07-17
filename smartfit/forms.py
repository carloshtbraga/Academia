from django import forms
from .models import Academia


class DateInput(forms.DateInput):
    input_type = "date"


class Formulario(forms.ModelForm):
    class Meta:
        model = Academia
        fields = ["nome", "endereco", "telefone", "foto", "plano", "nascimento"]
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Digite o nome do aluno"}),
            "telefone": forms.TextInput(
                attrs={"placeholder": "Digite o número de telefone"}
            ),
            "nascimento": DateInput(),
            "endereco": forms.TextInput(attrs={"placeholder": "Digite o endereço"}),
            "foto": forms.TextInput(attrs={"placeholder": "Digite a URL da foto"}),
        }

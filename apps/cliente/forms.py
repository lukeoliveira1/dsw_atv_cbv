from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields='__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control' }),
            'telefone' : forms.TextInput(attrs={'class': 'form-control' }),
            'endereco' : forms.TextInput(attrs={'class': 'form-control' }),
        }

class ClienteFilterForm(forms.Form):
    nome = forms.CharField(required=False)
     
    # adicionar a classe form-control para todos os campos
    def __init__(self, *args, **kwargs):
        super(ClienteFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
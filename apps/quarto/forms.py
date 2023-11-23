from django import forms

from .models import Quarto

class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields='__all__'
        widgets = {
            'apartamento' : forms.NumberInput(attrs={'class': 'form-control' }),
            'valor' : forms.NumberInput(attrs={'class': 'form-control' }),
        }
    
class QuartoFilterForm(forms.Form):
    apartamento = forms.IntegerField(required=False)
    
    # adicionar a classe form-control para todos os campos
    def __init__(self, *args, **kwargs):
        super(QuartoFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
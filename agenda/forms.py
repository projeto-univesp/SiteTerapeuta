from django import forms
from .models import Agenda

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['date', '_idTerapeuta', '_idPaciente'] 
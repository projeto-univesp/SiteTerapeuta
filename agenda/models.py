from django.db import models
from cadastro_paciente.models import CadastroPaciente

class Consulta(models.Model):
    paciente = models.ForeignKey(CadastroPaciente, on_delete=models.CASCADE)
    data_consulta = models.DateField()
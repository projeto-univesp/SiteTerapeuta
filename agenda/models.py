from django.db import models
from login_terapeuta.models import LoginTerapeuta
from cadastro_paciente.models import CadastroPaciente

class Agenda(models.Model):
    _id = models.AutoField(primary_key=True)
    date = models.DateField()
    _idTerapeuta = models.ForeignKey(LoginTerapeuta, on_delete=models.CASCADE)
    _idPaciente = models.ForeignKey(CadastroPaciente, on_delete=models.CASCADE)
# Generated by Django 5.0.4 on 2024-04-16 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastro_paciente", "0002_cadastropaciente_convenio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cadastropaciente",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
    ]

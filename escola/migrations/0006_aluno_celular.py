# Generated by Django 5.0 on 2023-12-31 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0005_matricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default='', max_length=11),
        ),
    ]

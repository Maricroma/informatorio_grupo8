# Generated by Django 3.0 on 2020-09-10 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votos', '0002_auto_20200909_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votos.Categoria'),
        ),
    ]

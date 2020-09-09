# Generated by Django 3.0 on 2020-09-09 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('votado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_votado', to=settings.AUTH_USER_MODEL)),
                ('votante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_votante', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

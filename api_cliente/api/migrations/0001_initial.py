# Generated by Django 4.1.3 on 2022-12-11 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=80)),
                ('nro_identificacion', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('monto_primera_compra', models.FloatField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.tipocliente')),
            ],
        ),
    ]

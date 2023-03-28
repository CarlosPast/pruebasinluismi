# Generated by Django 4.1.7 on 2023-03-22 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellidos', models.CharField(max_length=150)),
                ('tipo', models.CharField(choices=[('Mala', 'Mala'), ('Normal', 'Normal')], max_length=30)),
                ('numero', models.IntegerField()),
                ('fecha_salida', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='pruebita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djiangodeprueba.prueba')),
            ],
        ),
    ]
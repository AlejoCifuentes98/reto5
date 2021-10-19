# Generated by Django 3.2.7 on 2021-10-08 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes_proyectos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portafolio.categoria')),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-02 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('dni', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-12-05 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('curso', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('notas', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]

# Generated by Django 3.0.6 on 2022-10-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='models_accion_periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desde', models.DateField()),
                ('empresa', models.CharField(max_length=25)),
                ('accion', models.CharField(max_length=25)),
            ],
        ),
    ]

# Generated by Django 3.2.7 on 2022-04-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]

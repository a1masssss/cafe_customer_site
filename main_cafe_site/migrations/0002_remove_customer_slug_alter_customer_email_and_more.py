# Generated by Django 5.1.5 on 2025-02-10 13:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_cafe_site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='slug',
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=150, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=17),
        ),
    ]

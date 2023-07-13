# Generated by Django 4.2.2 on 2023-07-04 05:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_data_mobilenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='mobileNumber',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
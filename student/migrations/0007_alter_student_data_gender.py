# Generated by Django 4.2.2 on 2023-07-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_student_data_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='gender',
            field=models.CharField(max_length=7),
        ),
    ]

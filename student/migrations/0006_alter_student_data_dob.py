# Generated by Django 4.2.2 on 2023-07-04 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_student_data_mobilenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='dob',
            field=models.DateField(),
        ),
    ]
# Generated by Django 4.2.2 on 2023-07-03 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='mobileNumber',
            field=models.IntegerField(),
        ),
    ]
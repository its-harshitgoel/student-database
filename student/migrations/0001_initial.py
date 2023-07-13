# Generated by Django 4.2.2 on 2023-07-03 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('mobileNumber', models.IntegerField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('dob', models.DateField(max_length=8)),
            ],
        ),
    ]

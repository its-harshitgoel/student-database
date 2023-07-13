import django.core.validators
from django.db import migrations, models
import student.models

class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_data_mobilenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='mobileNumber',
            field=models.IntegerField()
        ),
    ]

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

class Student_data(models.Model):   
    #id = models.IntegerField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    gender = models.CharField(max_length=7)
    mobileNumber =models.BigIntegerField(
        validators=[
            MinValueValidator(1000000000),  
            MaxValueValidator(9999999999),  
        ],
        null=False)
    city=models.CharField(max_length=100)
    dob=models.DateField(max_length=8)
    
    def __str__(self):
        return self.lastName
    
from django.db import models
from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=20)
    student_code=models.CharField(max_length=15,unique=True)
   
    def __str__(self) -> str:
        return f"{self.student_name} - {self.student_code}"

    

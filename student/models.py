from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.AutoField()
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email =models.EmailField()
    code =models.PositiveSmallIntegerField()
    date_of_birth =models.DateField()
    country = models.CharField(max_length=20)
    bio =models.TextField()
    parentName = models.CharField(max_length=50)
    parentContact = models.CharField(max_length=20)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __email__(self):
        return {self.email}
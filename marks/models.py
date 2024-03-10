from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class mark(models.Model):
    userName=models.CharField(max_length=10)
    dateOfExam=models.DateField()
    Mark=models.IntegerField()

    def __str__(self):
        return self.userName



class student(models.Model):
    username=models.CharField(max_length=10)
    marks=models.ForeignKey(mark, on_delete=models.CASCADE,null=True,blank=True)
    bools=models.BooleanField(default=False)
   



        
    
        
    











    

    
    
from django.db import models

# Create your models here.
class Student(models.Model):  
    name=models.CharField(max_length=20)  
    age=models.IntegerField(max_length=3)
    
    def __unicode__(self):
        return self.name                          
                          
class Subject(models.Model):  
    student=models.ForeignKey(Student)  
    sub_name=models.CharField(max_length=20)  
    sub_num=models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.sub_name

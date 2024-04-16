from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=255)
    fee=models.IntegerField()
class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=255)
    student_address=models.CharField(max_length=255)
    student_age=models.IntegerField(null=True,blank=True)
    joining_date=models.DateField()
class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255)
    age=models.IntegerField(null=True)
    contact=models.CharField(max_length=255)
    img=models.ImageField(blank=True,upload_to="image/",null=True)
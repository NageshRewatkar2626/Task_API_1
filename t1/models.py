# from django.contrib.auth.models import User
from django.db import models


class EmployeeModel(models.Model):

	idno		=models.AutoField(primary_key=True)
	name		=models.CharField(max_length=30)
	contact_no	=models.IntegerField(unique=True)
	email		=models.CharField(max_length=100,unique=True)
	password	=models.CharField(max_length=20)
	# emp_photo   =models.FileField(upload_to='my_document/')

	# def __str__(self):
	# 	return self.name


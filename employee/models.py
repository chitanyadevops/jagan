from django.db import models
from datetime import date

class Employee(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	departmentid= models.ForeignKey('Department', on_delete=models.CASCADE)
	designation= models.CharField(max_length=200)
	salary=  models.CharField(max_length=10)
	phone_number= models.CharField(max_length=15)
	join_date= models.DateField('Date', blank=True)

	def __str__(self):
		return self.firstname


class Department(models.Model):
	department_name= models.CharField(max_length=200)
	def __str__(self):
		return self.department_name
					   
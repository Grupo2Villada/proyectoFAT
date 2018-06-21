# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from django.conf import settings
from django.db import models
from itertools import chain

# Create your models here.
STATUS_CHOICES = (
    ('1', "REGULAR"),
    ('2', "PRIMERA REINCORPORACION"),
    ('3', "SEGUNDA REINCORPORACION"),
    ('4', "LIBRE"),

)
DIVISION_CHOICES = (
    ("a", "A"),
    ("b", "B"),
    ("c", "C"),

)

YEAR_CHOICES = (
    (1, "Primero"),
    (2, "Segundo"),
    (3, "Tercero"),
    (4, "Cuarto"),
    (5, "Quinto"),
    (6, "Sexto"),
    (7, "Septimo"),

)

PERCENTAGE_CHOICES = (
    (0.25, "1/4"),
    (0.5, "1/2"),
    (0.75, "3/4"),
    (float(1), "1"),

)

ORIGIN_CHOICES = (
    (0, "Llegada tarde"),
    (1, "Retiro anticipado"),

)

class Year(models.Model):
	year_number = models.IntegerField(choices=YEAR_CHOICES)
	division = models.CharField(choices=DIVISION_CHOICES, max_length=1)

	def getStudents(self):
		results = Student.objects.filter(year=self)
		return results

	def __str__(self):
		return "{}-{}".format(self.year_number, self.division)

class Preceptor(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	internal_tel = models.IntegerField(blank=True)
	year = models.ManyToManyField(Year,blank=True,related_name='preceptores')

	def getYear(self):
		results = self.year.all()
		return results

	def getYearid(self):
		results = self.year.all().values_list('id', flat=True)
		return results


	def __str__(self):
		return "{} {}".format(self.user.first_name, self.user.last_name)

class Student(models.Model):
	first_name = models.CharField(max_length=12)
	last_name = models.CharField(max_length=25)
	dni = models.PositiveIntegerField(primary_key=True)
	student_tag = models.IntegerField()
	list_number = models.IntegerField()
	birthday = models.DateField()
	address = models.CharField(max_length=50)
	neighbourhood = models.CharField(max_length=50)
	city = models.CharField(max_length=50,blank=False, null=False)
	year = models.ForeignKey(Year)
	status = models.CharField(choices=STATUS_CHOICES, max_length= 1)
	food_obvs = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)

	def getAge(self):
		today = date.today()
		born=self.birthday
		return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

class Parent(models.Model):
	dni = models.IntegerField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	childs = models.ManyToManyField(Student,related_name='parents')
	address = models.CharField(max_length=50)
	neighbourhood = models.CharField(max_length=50)
	city = models.CharField(max_length=50,blank=False, null=False)

class Registro(models.Model):
	date = models.DateField()
	preceptor = models.ForeignKey(Preceptor)
	year = models.ForeignKey(Year)

	def __str__(self):
		return "{}".format(self.date)

class Relation(models.Model):
	registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	percentage = models.FloatField(choices=PERCENTAGE_CHOICES)
	origin = models.IntegerField(choices=ORIGIN_CHOICES)
	justified = models.BooleanField(default=False)	

	def __str__(self):
		return "{} {} {} {}".format(self.student, self.registro, self.percentage, self.justified)



# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ('1', "REGULAR"),
    ('2', "PRIMERA REINCORPORACION"),
    ('3', "SEGUNDA REINCORPORACION"),
    ('4', "LIBRE"),

)
DIVISION_CHOICES = (
    ('A', "A"),
    ('B', "B"),
    ('C', "C"),

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


class Person(models.Model):
	first_name = models.CharField(max_length=12)
	last_name = models.CharField(max_length=25)
	birthday = models.DateField()
	phone = models.CharField(max_length=15,blank=True, null=True)

	class Meta:
		abstract = True

class Year(models.Model):
	year_number = models.IntegerField(choices=YEAR_CHOICES)
	division = models.CharField(choices=DIVISION_CHOICES, max_length= 1)

class Preceptor(Person):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	internal_tel = models.IntegerField(blank=True, null=True)
	year = models.ManyToManyField(Year)

class Student(Person):
	dni = models.IntegerField()
	#legajo = Student tag
	student_tag = models.IntegerField()
	list_number = models.IntegerField()
	address = models.CharField(max_length=50)
	neighbourhood = models.CharField(max_length=50)
	city = models.CharField(max_length=50,blank=False, null=False)
	year = models.ForeignKey(Year)
	preceptor = models.ManyToManyField(Preceptor)
	status = models.CharField(choices=STATUS_CHOICES, max_length= 1)
	food_obvs = models.CharField(max_length=50)


class Absence(models.Model):
	justified = models.BooleanField(default=False)
	date = models.DateField(auto_now=True)
	percentage = models.FloatField(blank=True, null=True)
	student = models.ForeignKey(Student)

class Parent(Person):
	dni = models.IntegerField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	childs = models.ManyToManyField(Student)
	address = models.CharField(max_length=50)
	neighbourhood = models.CharField(max_length=50)
	city = models.CharField(max_length=50,blank=False, null=False)
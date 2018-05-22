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

class Preceptor(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	internal_tel = models.IntegerField(blank=True, null=True)
	year = models.ManyToManyField(Year)

	def __str__(self):
		return "{} {}".format(self.user.first_name, self.user.last_name)

class Student(models.Model):
	first_name = models.CharField(max_length=12)
	last_name = models.CharField(max_length=25)
	dni = models.IntegerField()
	student_tag = models.IntegerField()
	list_number = models.IntegerField()
	birthday = models.DateField()
	address = models.CharField(max_length=50)
	neighbourhood = models.CharField(max_length=50)
	city = models.CharField(max_length=50,blank=False, null=False)
	year = models.ForeignKey(Year)
	preceptor = models.ManyToManyField(Preceptor)
	status = models.CharField(choices=STATUS_CHOICES, max_length= 1)
	food_obvs = models.CharField(max_length=50)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)


class Absence(models.Model):
	origin = models.IntegerField(choices=ORIGIN_CHOICES)
	justified = models.BooleanField(default=False)
	date = models.DateField(auto_now=True)
	time = models.TimeField()
	percentage = models.FloatField(choices=PERCENTAGE_CHOICES)
	student = models.ForeignKey(Student)

class Parent(models.Model):
	dni = models.IntegerField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	childs = models.ManyToManyField(Student)
	address = models.CharField(max_length=50)
	neighbourhood = models.CharField(max_length=50)
	city = models.CharField(max_length=50,blank=False, null=False)
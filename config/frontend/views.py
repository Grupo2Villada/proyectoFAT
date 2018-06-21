# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from controlAsistencia.models import *
from django.contrib.auth.models import User
from controlAsistencia.forms import *
import datetime

# Create your views here.
def main(request):
	results={}
	try:
		preceptor = Preceptor.objects.get(user=request.user)
		results['years'] = preceptor.getYear()
		return render(request, 'main.html', results)
	except:
		return render(request, 'main.html')
def prueba(request):
	 return render(request, 'prueba.html')

def list_render(request, id):
	results={}
	year = Year.objects.get(id=id)
	preceptor = Preceptor.objects.get(user=request.user)
	results['students'] = year.getStudents()
	today_date = datetime.datetime.today()
	try:
		registro = Registro.objects.get(date=today_date, preceptor=preceptor, year=year)
	except Registro.DoesNotExist:
		registro = Registro.objects.create(date=today_date, preceptor=preceptor, year=year)
	return render(request, 'asistencia_lista.html', results)

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('main')
		else:
			return render(request, 'index.html')


def logout_user(request):
	logout(request)
	return redirect('/')

def register_user(request):
	if request.method == "POST":
		form = PreceptorForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		sec_pass = request.POST['sec_password']
		email = request.POST['email']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		if form.is_valid():	
			if password == sec_pass:
				user = User.objects.create_user(username, email, password)
				user.is_active = True
				user.first_name = first_name
				user.last_name = last_name
				user.save()
				internal_tel= form.cleaned_data.get("internal_tel")
				year= form.cleaned_data.get("year")
				preceptor = Preceptor(user=user,internal_tel=internal_tel)	
				preceptor.save()
				for i in year:
					preceptor.year.add(i)
			return redirect('/')
	else:
		form = PreceptorForm()
	return render(request, 'register.html', {'form': form})

def ausente(request):
	if request.method == "POST":
		today_date = datetime.datetime.today()
		preceptor = Preceptor.objects.get(user=request.user)
		student = Student.objects.get(dni=request.POST['student'])
		year= Student.objects.get(dni=request.POST['student']).year
		registro = Registro.objects.get(date=today_date, preceptor=preceptor, year=year)
		try:
			Relation.objects.get(registro=registro,student=student)
		except Relation.DoesNotExist:
			relation=Relation.objects.create(registro=registro, student=student, percentage=1, origin=0)
	return HttpResponse("ok")

def create_student(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			first_name= form.cleaned_data.get("first_name")
			last_name= form.cleaned_data.get("last_name")
			student_tag= form.cleaned_data.get("student_tag")
			list_number= form.cleaned_data.get("list_number")
			birthday= form.cleaned_data.get("birthday")
			address= form.cleaned_data.get("address")
			dni= form.cleaned_data.get("dni")
			neighbourhood= form.cleaned_data.get("neighbourhood")
			city= form.cleaned_data.get("city")
			yearqs= form.cleaned_data.get("year")
			status= form.cleaned_data.get("status")
			food_obvs= form.cleaned_data.get("food_obvs")
			year= Year.objects.get(id=yearqs)
			student = Student(first_name = first_name ,last_name = last_name, dni=dni , student_tag=student_tag ,list_number=list_number, birthday=birthday, address=address, neighbourhood=neighbourhood, year=year,city=city,status=status, food_obvs=food_obvs)
			student.save()
		return redirect('/')
	else:
		form = StudentForm()
	return render(request, 'create_student.html', {'form': form})

def index(request):
	return render(request, 'index.html')

def manage(request):
	return render(request, 'manage.html')

def update_preceptor(request):
	if request.method == "POST":
		form = PreceptorUpdateForm(request.POST)
		if form.is_valid():
			years=[]
			internal_tel= form.cleaned_data.get("internal_tel")
			year= form.cleaned_data.get("year")	
			preceptor_id= form.cleaned_data.get("preceptor_id")
			preceptor=Preceptor.objects.filter(id=preceptor_id)
			preceptor_year=Preceptor.objects.get(id=preceptor_id)
			preceptor_year.year.clear()
			# if request.POST["username"]!= preceptor_year.user.username: probar performance
			preceptor_year.user.username = request.POST["username"]
			preceptor_year.user.first_name = request.POST["first_name"]
			preceptor_year.user.last_name = request.POST["last_name"]
			preceptor_year.user.email = request.POST["email"]
			preceptor_year.user.save()

			for i in year:
				preceptor_year.year.add(i)
			preceptor.update(internal_tel=internal_tel)
		return redirect('/')
	else:
		years = []
		results= {}
		id=request.GET.get('preceptor')
		results["id"] = id
		preceptor = Preceptor.objects.get(id=id)
		results["username"]= preceptor.user.username
		results["first_name"]= preceptor.user.first_name
		results["last_name"]= preceptor.user.last_name
		results["email"]= preceptor.user.email
		qs_year = preceptor.getYearid()
		for i in qs_year:
			years.append(i)
		form = PreceptorUpdateForm(initial={'preceptor_id':id,'internal_tel':preceptor.internal_tel, 'year':years})
		results["form"]= form
	return render(request,'update_preceptor.html', results)

def preceptor_list(request):
	preceptors=Preceptor.objects.all()
	return render(request,'preceptor_list.html',{ 'preceptors':preceptors })

def student_list(request):
	students=Student.objects.all().order_by('birthday','last_name','first_name')
	return render(request,'student_list.html',{ 'students':students })

def update_student(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			first_name= form.cleaned_data.get("first_name")
			dni= form.cleaned_data.get("dni")
			student=Student.objects.filter(dni=dni)
			last_name= form.cleaned_data.get("last_name")
			student_tag= form.cleaned_data.get("student_tag")
			list_number= form.cleaned_data.get("list_number")
			birthday= form.cleaned_data.get("birthday")
			address= form.cleaned_data.get("address")
			neighbourhood= form.cleaned_data.get("neighbourhood")
			city= form.cleaned_data.get("city")
			year= form.cleaned_data.get("year")
			status= form.cleaned_data.get("status")
			food_obvs= form.cleaned_data.get("food_obvs")
			student.update(first_name=first_name, last_name=last_name, student_tag=student_tag, list_number=list_number, birthday=birthday, address=address, neighbourhood=neighbourhood, city=city, year=year, status=status, food_obvs=food_obvs)
		return redirect('/')
	else:
		results= {}
		dni=request.GET.get('student')
		results["dni"] = dni
		student = Student.objects.get(dni=dni)
		age = student.getAge()
		form = StudentForm(initial={'first_name':student.first_name, 'last_name':student.last_name, 'dni':student.dni, 'student_tag':student.student_tag, 'list_number':student.list_number, 'birthday':student.birthday, 'address':student.address, 'neighbourhood':student.neighbourhood, 'city':student.city, 'year':student.year.id, 'status':student.status,'food_obvs':student.food_obvs})
		results["form"]= form
	return render(request,'update_student.html', results)

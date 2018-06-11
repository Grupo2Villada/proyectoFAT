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
def index(request):
	results={}
	preceptor = Preceptor.objects.get(user=request.user)
	results['years'] = preceptor.getYear()
	return render(request, 'main.html', results)

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
	return redirect('index')

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
				print "password match"
				user = User.objects.create_user(username, email, password)
				user.is_active = True
				user.first_name = first_name
				user.last_name = last_name
				user.save()
				print "form"
				internal_tel= form.cleaned_data.get("internal_tel")
				year= form.cleaned_data.get("year")
				print year
				preceptor = Preceptor(user=user,internal_tel=internal_tel)	
				preceptor.save()
				test(preceptor,year)
			return redirect('/')
	else:
		form = PreceptorForm()
	return render(request, 'register.html', {'form': form})

def test(preceptor,year):
	print preceptor.user
	for i in year:
		preceptor.year.add(i)

def ausente(request):
	print "ausente"
	if request.method == "POST":
		today_date = datetime.datetime.today()
		preceptor = Preceptor.objects.get(user=request.user)
		student = Student.objects.get(id=request.POST['student'])
		year= Student.objects.get(id=request.POST['student']).year
		registro = Registro.objects.get(date=today_date, preceptor=preceptor, year=year)
		try:
			Relation.objects.get(registro=registro,student=student)
		except Relation.DoesNotExist:
			relation=Relation.objects.create(registro=registro, student=student, percentage=1, origin=0)
	return HttpResponse("ok")

def main(request):
	return render(request, 'index.html')
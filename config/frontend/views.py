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
from django.utils import timezone
from controlAsistencia.models import *
from django.contrib.auth.models import User
import datetime
from datetime import timedelta
import sys
#import xlwt
from django.db.models.functions import Concat
from django.db.models.functions import Upper
import calendar
from django.core.mail import send_mail, EmailMessage
from collections import Counter
if 'makemigrations' not in sys.argv and 'migrate' not in sys.argv:
	from controlAsistencia.forms import *

# Create your views here.
def main(request):
	results={}
	try:
		preceptor = Preceptor.objects.get(user=request.user)
		results['years'] = preceptor.getYear().order_by('year_number','division')
		print results['years']
		return render(request, 'main.html', results)
	except:
		return render(request, 'main.html')

def prueba(request):
	return render(request, 'prueba.html')

def asistencia(request,id):
	results={}
	results['id']=id
	return render(request,'asistencia.html',results)

def list_render(request,id):

	results={}
	ausentes = []
	presentes=[]

	today_date = datetime.date.today()
	year = Year.objects.get(id=id)
	preceptor = Preceptor.objects.get(user=request.user)
	students = year.getStudents().order_by('last_name','first_name')
	faltas1 = Absence.objects.filter(date = today_date , percentage=1, student__year=year) 
	faltas2 = Absence.objects.filter(date = today_date, student__year=year, origin = 2)  
	faltas = faltas1 | faltas2

	for i in faltas:
		ausentes.append(i.student)
	presentes = list(set(students)-set(ausentes))
	if (ausentes==[]):
		results['students']= students
	else:
		results['students']= presentes
	return render(request, 'asistencia_lista.html', results)


def list_render2(request,id):
	
	#results['students'] = year.getStudents().order_by('last_name','first_name')


	results={}
	ausentes = []
	presentes=[]

	today_date = datetime.date.today()
	year = Year.objects.get(id=id)
	preceptor = Preceptor.objects.get(user=request.user)
	students = year.getStudents().order_by("room_order")
	faltas1 = Absence.objects.filter(date = today_date , percentage=1, student__year=year) 
	faltas2 = Absence.objects.filter(date = today_date, student__year=year, origin = 2)  
	faltas = faltas1 | faltas2

	for i in faltas:
		ausentes.append(i.student)
	presentes = list(set(students)-set(ausentes))
	if (ausentes==[]):
		results['students']= students
	else:
		results['students']= presentes
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
				try :
					User.objects.get(username = username)
				except User.DoesNotExist:
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
				return redirect('manage')
	else:
		form = PreceptorForm()
	return render(request, 'register.html', {'form': form})

def ausente(request):
	if request.method == "POST":
		today_date = datetime.date.today()
		today_time = datetime.datetime.now().time()
		preceptor = Preceptor.objects.get(user=request.user)
		student = Student.objects.get(dni=request.POST['student'])
		year= Student.objects.get(dni=request.POST['student']).year
		try:
			Absence.objects.get(date=today_date, preceptor=preceptor, year=year,student=student)
		except Absence.DoesNotExist:
			absence=Absence.objects.create(date=today_date,time=today_time, preceptor=preceptor, year=year, student=student, percentage=1, origin=0)
	return HttpResponse("ok")

def undo_falta(request):
	if request.method == "POST":
		today_date = datetime.date.today()
		preceptor = Preceptor.objects.get(user=request.user)
		student = Student.objects.get(dni=request.POST['student'])
		year= Student.objects.get(dni=request.POST['student']).year
		try:
			abse=Absence.objects.get(date=today_date, preceptor=preceptor, year=year,student=student)
			abse.delete()
		except Absence.DoesNotExist:
			pass
		return HttpResponse("ok")

def create_student(request):
	print "view"
	if request.method == "POST":
		print "post"
		form = CreateStudentForm(request.POST)
		if form.is_valid():
			print "valid"
			first_name= form.cleaned_data.get("first_name")
			last_name= form.cleaned_data.get("last_name")
			student_tag= form.cleaned_data.get("student_tag")
			list_number= form.cleaned_data.get("list_number")
			room_order = form.cleaned_data.get("room_order")
			birthday= form.cleaned_data.get("birthday")
			address= form.cleaned_data.get("address")
			dni= form.cleaned_data.get("dni")
			neighbourhood= form.cleaned_data.get("neighbourhood")
			city= form.cleaned_data.get("city")
			yearqs= form.cleaned_data.get("year")
			status= form.cleaned_data.get("status")
			food_obvs= form.cleaned_data.get("food_obvs")
			year= Year.objects.get(id=yearqs)
			try: 
				a=Student.objects.get(dni=dni)
			except Student.DoesNotExist:
				student = Student(first_name = first_name ,last_name = last_name, dni=dni , student_tag=student_tag ,list_number=list_number,room_order=room_order ,birthday=birthday, address=address, neighbourhood=neighbourhood, year=year,city=city,status=status, food_obvs=food_obvs)
				student.save()
			return redirect('manage')
	else:
		form = CreateStudentForm()
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
		return redirect('manage')
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
			id=form.cleaned_data.get("id")
			first_name= form.cleaned_data.get("first_name")
			dni= form.cleaned_data.get("dni")
			last_name= form.cleaned_data.get("last_name")
			student_tag= form.cleaned_data.get("student_tag")
			list_number= form.cleaned_data.get("list_number")
			room_order= form.cleaned_data.get("room_order")
			birthday= form.cleaned_data.get("birthday")
			address= form.cleaned_data.get("address")
			neighbourhood= form.cleaned_data.get("neighbourhood")
			city= form.cleaned_data.get("city")
			year= form.cleaned_data.get("year")
			status= form.cleaned_data.get("status")
			food_obvs= form.cleaned_data.get("food_obvs")
			student=Student.objects.filter(id=id)
			student.update(first_name=first_name, last_name=last_name, student_tag=student_tag, list_number=list_number, room_order=room_order,birthday=birthday, dni=dni,address=address, neighbourhood=neighbourhood, city=city, year=year, status=status, food_obvs=food_obvs)
		return redirect('manage')
	else:
		results= {}
		id=request.GET.get('student')
		results["id"] = id
		student = Student.objects.get(id=id)
		age = student.getAge()
		form = StudentForm(initial={'first_name':student.first_name, 'last_name':student.last_name, 'dni':student.dni, 'student_tag':student.student_tag, 'list_number':student.list_number, 'room_order':student.room_order,'birthday':student.birthday, 'address':student.address, 'neighbourhood':student.neighbourhood, 'city':student.city, 'year':student.year.id, 'status':student.status,'food_obvs':student.food_obvs})
		results["form"]= form
	return render(request,'update_student.html', results)

def late_arrival(request):
	if request.method == "POST":
		absence_time = Absence.objects.get(id=request.POST['absence'])
		""" PARA FUTURO CALCULO DE FALTAS

		print "dia falta "+ str(absence_time.date)
		print "hoy dia"+ str(datetime.date.today())
		print "hora falta "+ str(absence_time.time)
		print "hoy hora "+ str(datetime.datetime.now().time())
		a = datetime.datetime.now().time()- absence_time.time
		print "dif" + str(a)
		"""
		absence_q = Absence.objects.filter(id=request.POST['absence'])

		now = datetime.datetime.now().time()
		cuarto = now.replace(hour=7, minute= 55 , second= 0) 
		media = now.replace(hour=8, minute= 05 , second= 0) 
		tres_cuartos = now.replace(hour=11, minute= 00 , second= 0) 
		completa = now.replace(hour=13, minute= 0 , second= 0) 

		if now > a15am:
			absence_q.update(percentage=1)
			
		elif now > a12am:
			absence_q.update(percentage=0.75)

		elif now > a10_30am:
			absence_q.update(percentage=0.5)

		elif now > cuarto:
			absence_q.update(percentage=0.25)

		
	return HttpResponse("ok")

def late_render(request, id):
	results={}
	year = Year.objects.get(id=id)
	preceptor = Preceptor.objects.get(user=request.user)
	students = year.getStudents()
	today_date = datetime.date.today()
	absences = Absence.objects.filter(date=today_date, preceptor=preceptor, year=year).order_by('student__last_name','student__first_name')
	results['absences']= absences
	return render(request, 'llegada_tarde.html', results)

def early_retirement(request):
	if request.method == "POST":
		student = Student.objects.get(dni=request.POST['student'])
		year = Year.objects.get(id=student.year.id)
		preceptor = Preceptor.objects.get(user = request.user)
		today_date = datetime.date.today()
		now = datetime.datetime.now().time()
		a9am = now.replace(hour=9, minute= 0 , second= 0) 
		a12_30am = now.replace(hour=12, minute= 30 , second= 0) 
		a15_20am = now.replace(hour=15, minute= 20 , second= 0) 

		if now < a9am:
			Absence.objects.create(percentage=0.75,student=student,origin=2,date=today_date,time=now,preceptor=preceptor,year=year, justified=True)
			
		elif now < a12_30am:
			Absence.objects.create(percentage=0.50,student=student,origin=2,date=today_date,time=now,preceptor=preceptor,year=year, justified=True)

		elif now < a15_20am:
			Absence.objects.create(percentage=0.25,student=student,origin=2,date=today_date,time=now,preceptor=preceptor,year=year, justified=True)

		
	return HttpResponse("ok")

def early_render(request, id):
	results={}
	ausentes = []
	presentes=[]

	today_date = datetime.date.today()
	year = Year.objects.get(id=id)
	preceptor = Preceptor.objects.get(user=request.user)
	students = year.getStudents()
	faltas1 = Absence.objects.filter(date = today_date , percentage=1, student__year=year) 
	faltas2 = Absence.objects.filter(date = today_date, student__year=year, origin = 2)  
	faltas = faltas1 | faltas2

	for i in faltas:
		ausentes.append(i.student)
	print ausentes
	print students
	print presentes
	presentes = list(set(students)-set(ausentes))
	print presentes
	if (ausentes==[]):
		results['students']= students
	else:
		results['students']= presentes

	return render(request, 'retiro_anticipado.html', results)

def justification_render(request, id):
	results={}
	year = Year.objects.get(id=id)
	if request.user.is_staff:
		absences = Absence.objects.filter(year=year, justified=False).order_by('date')
		results['absences']= absences
		return render(request, 'justificar_falta.html', results)
	else:	
		today_date = datetime.date.today()
		n = 2
		fecha = today_date - timedelta(days=n)
		print fecha
		absences = Absence.objects.filter(year=year,date__gte=fecha, justified=False).order_by('date')
		results['absences']= absences
		return render(request, 'justificar_falta.html', results)


def justify(request):
		absence_q = Absence.objects.filter(id=request.POST['absence'])
		absence_q.update(justified=True)
		return HttpResponse("ok")

def export_users_xls(year_number,division):
	today_date = datetime.date.today()
	month = today_date.month
	month_name = datetime.date(today_date.year,today_date.month, 1).strftime('%B')
	students = Student.objects.filter(year__year_number=year_number, year__division=division).order_by("last_name")
	#response = HttpResponse(content_type='application/ms-excel')
	#response['Content-Disposition'] = 'attachment; filename={}-{}{}.xls'.format(month_name, year, division)
	wb = xlwt.Workbook(encoding='utf-8')	

	ws = wb.add_sheet("{}".format(today_date.month), cell_overwrite_ok=True)
	style1 = xlwt.XFStyle()
	pattern = xlwt.Pattern()
	pattern.pattern = xlwt.Pattern.SOLID_PATTERN
	pattern.pattern_fore_colour = xlwt.Style.colour_map['yellow']
	style1.pattern = pattern

	borders= xlwt.Borders()
	borders.left= 7
	borders.right= 7
	borders.top= 7
	borders.bottom= 7
	style1.borders = borders

	# Sheet header, first row
	row_num = 0
	style1.font.bold = True
	ws.col(0).width = int(20*265)
	ws.col(1).width = int(10*256)
	cantidadDias=calendar.monthrange(today_date.year,today_date.month)[1]
	style3 = xlwt.XFStyle()
	style3.borders = borders
	cantidadAlumnos= students.count()
	weekno = datetime.datetime.today().weekday()
	#Columnas default
	columns = ['Nombre', 'Año']
	#MES CON 31 DIAS
	if(cantidadDias==31):
		#Agregar 31 columnas para los dias
		for i in range(1,32):
			columns.append(i)
		for j in range(2,33):
			ws.col(j).width = int(20*50)
			# for alumno in range(1,cantidadAlumnos+1):
			# 	for dia in range(1,31):
			# 		print datetime.date(day=dia, month=month, year=today_date.year)
			# 		if datetime.date(day=dia, month=month, year=today_date.year).weekday()<5:	
			# 			ws.write(alumno,j,"P",style3)
			# 		else:
			# 			ws.write(alumno,j," ",style3)
		for dia in range (1,32):
			if datetime.date(day=dia, month=month, year=today_date.year).weekday()<5:
				for alumno in range(1,cantidadAlumnos+1):
					ws.write(alumno,dia+1,"P",style3)
			else:
				for alumno in range(1,cantidadAlumnos+1):
					ws.write(alumno,dia+1," ",style3)



			nro=0
			for student in students:
				nro+=1
				ws.write(nro, 0, "{}, {}".format(student.last_name.upper(),student.first_name)	,style3)
				ws.write(nro, 1, "{}".format(student.year),style3)

				absences = student.getAbsence().filter(date__month=month)
				if absences:
					for absence in absences:
						#ws.write(0, absence.date.day, "{}".format(absence.date.day))    ????no se que es esto
						if absence.justified == True and absence.percentage == 1:
							ws.write(nro, absence.date.day+1, "{}".format("AJ"),style3)
						elif absence.justified == False and absence.percentage == 1:
							ws.write(nro, absence.date.day+1, "{}".format("A"),style3)
						elif absence.justified == True and absence.percentage == 0.75:
							ws.write(nro, absence.date.day+1, "{}".format("CJ"),style3)
						elif absence.justified == False and absence.percentage == 0.75:
							ws.write(nro, absence.date.day+1, "{}".format("C"),style3)
						elif absence.justified == True and absence.percentage == 0.5:
							ws.write(nro, absence.date.day+1, "{}".format("MJ"),style3)
						elif absence.justified == False and absence.percentage == 0.5:
							ws.write(nro, absence.date.day+1, "{}".format("M"),style3)
						elif absence.justified == True and absence.percentage == 0.25:
							ws.write(nro, absence.date.day+1, "{}".format("RJ"),style3)
						elif absence.justified == False and absence.percentage == 0.25:
							ws.write(nro, absence.date.day+1, "{}".format("R"),style3)
		for col_num in range(len(columns)):
		    ws.write(row_num, col_num, columns[col_num], style1)

	#MES CON 30 DIAS
	elif(cantidadDias==30):
		#Agregar 31 columnas para los dias
		for i in range(1,31):
			columns.append(i)
		for j in range(2,32):
			ws.col(j).width = int(20*50)
			# for alumno in range(1,cantidadAlumnos+1):
			# 	for dia in range(1,31):
			# 		print datetime.date(day=dia, month=month, year=today_date.year)
			# 		if datetime.date(day=dia, month=month, year=today_date.year).weekday()<5:	
			# 			ws.write(alumno,j,"P",style3)
			# 		else:
			# 			ws.write(alumno,j," ",style3)
		for dia in range (1,31):
			if datetime.date(day=dia, month=month, year=today_date.year).weekday()<5:
				for alumno in range(1,cantidadAlumnos+1):
					ws.write(alumno,dia+1,"P",style3)
			else:
				for alumno in range(1,cantidadAlumnos+1):
					ws.write(alumno,dia+1," ",style3)



			nro=0
			for student in students:
				nro+=1
				ws.write(nro, 0, "{}, {}".format(student.last_name.upper(),student.first_name)	,style3)
				ws.write(nro, 1, "{}".format(student.year),style3)

				absences = student.getAbsence().filter(date__month=month)
				if absences:
					for absence in absences:
						#ws.write(0, absence.date.day, "{}".format(absence.date.day))    ????no se que es esto
						if absence.justified == True and absence.percentage == 1:
							ws.write(nro, absence.date.day+1, "{}".format("AJ"),style3)
						elif absence.justified == False and absence.percentage == 1:
							ws.write(nro, absence.date.day+1, "{}".format("A"),style3)
						elif absence.justified == True and absence.percentage == 0.75:
							ws.write(nro, absence.date.day+1, "{}".format("CJ"),style3)
						elif absence.justified == False and absence.percentage == 0.75:
							ws.write(nro, absence.date.day+1, "{}".format("C"),style3)
						elif absence.justified == True and absence.percentage == 0.5:
							ws.write(nro, absence.date.day+1, "{}".format("MJ"),style3)
						elif absence.justified == False and absence.percentage == 0.5:
							ws.write(nro, absence.date.day+1, "{}".format("M"),style3)
						elif absence.justified == True and absence.percentage == 0.25:
							ws.write(nro, absence.date.day+1, "{}".format("RJ"),style3)
						elif absence.justified == False and absence.percentage == 0.25:
							ws.write(nro, absence.date.day+1, "{}".format("R"),style3)
		for col_num in range(len(columns)):
		    ws.write(row_num, col_num, columns[col_num], style1)
	# Sheet body, remaining rows


	style = xlwt.XFStyle()
	style.borders = borders
	style.alignment.wrap = 1

	wb.save(settings.MEDIA_ROOT+'{}-{}{}.xls'.format(month_name, year_number, division))
	send_mail(settings.MEDIA_ROOT+'{}-{}{}.xls'.format(month_name, year_number, division))
	return redirect('manage')

def send_mail(file,body,title,reciever):
	msg = EmailMessage(title,body,'test.asistencia@gmail.com', reciever)
	if file:
		msg.attach_file(file)
	msg.send()

def excel(request):
	for i in Year.objects.all():
		export_users_xls(i.year_number,i.division)
	return HttpResponse("ok")

def comedor(request):	
	today_date = datetime.date.today()
	absences = Absence.objects.filter(date=today_date)
	ausentes = str(len(absences))
	x= []
	observaciones=[]
	for i in absences:
		if i.student.food_obvs:
			x.append(i.student.food_obvs)
	y=Counter(x)
	for key, value in y.iteritems():
		observaciones.append(key+": "+str(value))
	send_mail(file=None,body="Alumnos ausentes: " +ausentes+"\n\n<b>Observaciones:</b>\n"+"\n".join(observaciones),title="Alumnos comedor - {} ".format(today_date),reciever=['juli.luna1999@gmail.com','nikobazan@gmail.com'])
	return redirect("manage")

def crontry():
	print "CRON_____________________"

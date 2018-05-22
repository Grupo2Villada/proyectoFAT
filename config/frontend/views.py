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

# Create your views here.
def index(request):
	 return render(request, 'base.html')

def prueba(request):
	 return render(request, 'prueba.html')

def list_render(request):
	return render(request, 'asistencia_lista.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

def register_user(request):
    if request.method == "POST":
        form = PreceptorForm(request.POST)
        if form.is_valid():
            post = form.instance
            username = request.POST['username']
            password = request.POST['password']
            sec_pass = request.POST['sec_password']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            if password == sec_pass:
                user = User.objects.create_user(username, email, password)
                user.is_active = False
                user.first_name = first_name
                user.last_name = last_name
                if (user.save()):
                    print "user"
                preceptor = Preceptor(user=user,internal_tel=post.internal_tel,year=year)
                if(preceptor.save()):
                    print "preceptor"
                if(post.save()):
                    print "save(?"
    else:
        form = PreceptorForm()
    return render(request, 'base.html', {'form':form})
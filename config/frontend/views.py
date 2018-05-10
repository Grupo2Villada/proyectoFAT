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


# Create your views here.
def index(request):
	 return render(request, 'base.html')

def prueba(request):
	 return render(request, 'prueba.html')


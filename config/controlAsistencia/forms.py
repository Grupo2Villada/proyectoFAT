from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class PreceptorForm(forms.Form):
	internal_tel = forms.IntegerField(label='Internal tel', min_value=1)
	year = forms.MultipleChoiceField(widget=forms.SelectMultiple,choices=[
	(year.pk, year) for year in Year.objects.all()])

class PreceptorUpdateForm(forms.Form):
	preceptor_id = forms.IntegerField()
	internal_tel = forms.IntegerField(label='Internal tel')
	year = forms.MultipleChoiceField(widget=forms.SelectMultiple,choices=[
	(year.pk, year) for year in Year.objects.all()])

class StudentForm(forms.Form):
	id = forms.IntegerField(min_value=1)
	first_name = forms.CharField(max_length=12)
	last_name = forms.CharField(max_length=25)
	dni = forms.IntegerField(max_value=99999999, min_value=1)
	student_tag = forms.IntegerField(max_value=99999, min_value=1)
	list_number = forms.IntegerField(max_value=45, min_value=1)
	birthday = forms.DateField(widget = forms.SelectDateWidget(years=range(1900,2019)))
	address = forms.CharField(max_length=50)
	neighbourhood = forms.CharField(max_length=50)
	city = forms.CharField(max_length=50)
	year = forms.ChoiceField(widget=forms.Select, choices=[(year.pk, year) for year in Year.objects.all()])
	status = forms.ChoiceField(widget=forms.Select, choices=STATUS_CHOICES)
	food_obvs = forms.CharField(required=False)
    
class CreateStudentForm(forms.Form):
	first_name = forms.CharField(max_length=12)
	last_name = forms.CharField(max_length=25)
	dni = forms.IntegerField(max_value=99999999, min_value=1)
	student_tag = forms.IntegerField(max_value=99999, min_value=1)
	list_number = forms.IntegerField(max_value=45, min_value=1)
	birthday = forms.DateField(widget = forms.SelectDateWidget(years=range(1900,2019)))
	address = forms.CharField(max_length=50)
	neighbourhood = forms.CharField(max_length=50)
	city = forms.CharField(max_length=50)
	year = forms.ChoiceField(widget=forms.Select, choices=[(year.pk, year) for year in Year.objects.all()])
	status = forms.ChoiceField(widget=forms.Select, choices=STATUS_CHOICES)
	food_obvs = forms.CharField(required=False)
    
    
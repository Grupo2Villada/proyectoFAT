from .models import *
from django import forms
from django.forms import ModelForm
class PreceptorForm(forms.Form):
	internal_tel = forms.IntegerField(label='Internal tel')
	year = forms.MultipleChoiceField(widget=forms.SelectMultiple,choices=[
	(year.pk, year) for year in Year.objects.all()])

class PreceptorUpdateForm(forms.Form):
	preceptor_id = forms.IntegerField()
	internal_tel = forms.IntegerField(label='Internal tel')
	year = forms.MultipleChoiceField(widget=forms.SelectMultiple,choices=[
	(year.pk, year) for year in Year.objects.all()])

class StudentForm(ModelForm):
	class Meta:
		model= Student
		fields='__all__'

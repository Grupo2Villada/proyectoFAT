from .models import *
from django import forms
from django.forms import ModelForm
class PreceptorForm(forms.Form):
	internal_tel = forms.IntegerField(label='Internal tel')
	year = forms.MultipleChoiceField(widget=forms.SelectMultiple,choices=[
	(year.pk, year) for year in Year.objects.all()])


class YearForm(ModelForm):
	class Meta:	
		model = Year
		fields = '__all__' 
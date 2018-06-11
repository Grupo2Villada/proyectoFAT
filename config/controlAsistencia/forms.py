from .models import *
from django import forms
class PreceptorForm(forms.Form):
	internal_tel = forms.IntegerField(label='Internal tel')
	year = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[
	(year.pk, year) for year in Year.objects.all()])
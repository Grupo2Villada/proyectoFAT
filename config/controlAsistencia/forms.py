from django.forms import ModelForm
from .models import *

class PreceptorForm(ModelForm):
	class Meta:	
		model = Preceptor
		fields = '__all__'
		exclude = ['user']	
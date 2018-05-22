from django.forms import ModelForm
from .models import *

class PreceptorForm(ModelForm):
	class Meta:	
		model = Preceptor
		fields = ['internal_tel', 'year']
from django import forms
from .models import  covid

class MyForm(forms.ModelForm):
	class Meta():
		model = covid 
		fields = ['nom','prenom','willaya','commune','willayaTravail','communeTravail','age','infection']
			
		
       


	

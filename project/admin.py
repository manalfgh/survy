from django.contrib import admin
from .models import  covid

# Register your models here.
class covidAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('nom','prenom','infection', 'willaya','commune','willayaTravail','communeTravail','age')

admin.site.register(covid, covidAdmin)  



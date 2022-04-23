from django.contrib import admin
from matplotlib.pyplot import cla

# Register your models here.
from .models import Diplomas, Alumnos

class Alumno_data(admin.ModelAdmin):
    list_display=("first_name","last_name","email","course","pub_date")
    date_hierarchy = "pub_date"
    list_filter = ("email",'course')

class Diploma_data(admin.ModelAdmin):
    list_display=('diplom_hash',)

admin.site.register(Diplomas, Diploma_data)
admin.site.register(Alumnos, Alumno_data)
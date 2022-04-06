from django.contrib import admin
from employee.models.register import Register
# Register your models here.

class Reg(admin.ModelAdmin):
    list_display = ['name','email','password','phone','distt','state']

admin.site.register(Register,Reg)

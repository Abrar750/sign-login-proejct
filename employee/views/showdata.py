from django.shortcuts import render
from django.views import View
from employee.models.register import Register

class Show(View):
    def get(self,request):
        data = Register.objects.all()
        return render(request,'showdata.html',{'employee':data})
    

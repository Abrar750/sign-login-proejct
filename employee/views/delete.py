from django.shortcuts import redirect, render
from employee.models.register import Register


def delete(request,id):
    user = Register.objects.get(id = id)
    user.delete()
    return redirect('showdata')




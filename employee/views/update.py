
from django.shortcuts import redirect, render
from employee.models.register import Register


def Edit(request,id):
    user = Register.objects.get(id = id)
    data = {
        'user':user
    }
    return render(request,"update.html",data)

def update(request,id):
    user = Register.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        user.name = name
        user.email = email
        user.phone = phone
        user.city = city
        user.state = state
        user.save()
        return redirect('/show/')
import email
from django.shortcuts import redirect, render
from django.views import View
from employee.models.register import Register
from django.contrib.auth.hashers import make_password
class Regis(View):
    def get(self,request):
        return render(request,"register.html")
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get("password")
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        value={
            'name':name,
            'email':email,
            'password':password,
            'phone':phone,
            'city':city,
            'state':state
        }
        error = None
        if not name:
            error = "Required name.."
        elif len(name) < 3:
            error = "Requeired name length.."
        elif not email:
            error = "Required email.."
        elif not password:
            error = "Required password..."
        elif not phone:
            error = "Required phone.."
        elif not city:
            error = "Required city.."
        elif not state:
            error = "Required state.."
        elif Register.isExists(email):
            error = 'Email all ready exists..'

        if not error:
            customer = Register(name=name,email=email,password=password,phone=phone,distt=city,state=state)
            customer.password = make_password(password)
            customer.save()
            return redirect("Register")
        else:
            data = {
                'error':error,
                'value':value
            }
            return render(request,'register.html',data)




from django.shortcuts import redirect, render
from django.views import View
from employee.models.register import Register
from django.contrib.auth.hashers import check_password
class Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Register.get_email_by_id_email(email)
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                return redirect('/show/')
            else:
                error = "Password is not valid.."
        else:
            error="Email and password no valid..."
        data={
            'error':error
        }
        return render(request,'login.html',data)
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method=="post":
        first_name=request.POST.get['firstname']
        last_name = request.POST.get['lastname']
        username = request.POST.get['username']
        email = request.POST.get['email']
        password1 = request.POST.get['password1']
        password2 = request.POST.get['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password1=password1,firstname=first_name,lastname=last_name,email=email)
                user.save()
                print('user created')
        else:
            print('password not matched')
            return redirect('register')
    else:
        return render(request,'register.html')



def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'index.html')



from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
#from django.conf import 
from .models import Destination
# Create your views here.
def index(request):
    dests = Destination.objects.all()
   
    return render(request,'index.html',{'dests': dests})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,'username or password is incorrect')
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username):
                messages.info(request,'User already exists')
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,password = password1, first_name = first_name, last_name = last_name,email = email)
                user.save()
                return redirect('login')    
        else:
            messages.info(request,'password not matched')

    else: 
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def destinations(request):
    return render(request,'destination.html')
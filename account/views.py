from django.shortcuts import render,redirect
from django.contrib import  messages
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        username = request.POST['username']
        if User.objects.filter(email=email).exists():
            messages.info(request,'email exists already')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'username exists already')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=name)
            user.save();
            print('user created')
            return redirect(request,'login.html')
    else:

        return render(request,'register.html')
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
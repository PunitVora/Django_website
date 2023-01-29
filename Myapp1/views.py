from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout 
from django.contrib import messages


# Create your views here.

#what ever we do in this function will happen to the url it is assigned.
#path('',views.index, name ='index')

# function for index.html 
def Index (request):
    return render(request, 'index.html' )

# function for register
def Register(request) :
    if request.method == "POST" :

        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists() :
                messages.info(request, 'Email already exists!!')
                return redirect('Register')
            elif User.objects.filter(username=username).exists() :
                messages.info(request, 'Username already exists!!')
                return redirect('Register')
            else:
                try:
                    user = User.objects.create_user(username=username,email=email , password=password )
                    user.save()
                    return redirect('Login')
                except :
                    messages.info(request, "Please don't leave any fields empty!!")
                    return redirect('Register')

        else:   
                messages.info(request, 'Password did not match!!')
                return redirect('register')
        
         

    else:
        return render(request, 'register.html')

# function for login.html 
def Login (request) :
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)

        if user is not None :
            login(request, user)
            return redirect('/') 
        else:
            messages.info(request,'Invalid Credentials!!')
            return redirect('Login')
           
         
    else:    
        return render(request, 'login.html' )

# function for logout.html 
def Logout (request):
    logout(request)
    return redirect('/') #redirect to home

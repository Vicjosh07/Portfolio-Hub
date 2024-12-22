from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method == "POST":
        get_email = request.POST.get("email")
        get_user = request.POST.get("user")
        get_password = request.POST.get("pass1")
        get_confirm_password = request.POST.get("pass2")
        if get_password != get_confirm_password:
            messages.info(request, 'Password is not matching')
            return redirect('/auth/signup/')

        try:
            if User.objects.get(email=get_email):
                messages.error(request, 'Email used already')
                return redirect('/auth/signup/')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(get_user, get_email, get_password)
        myuser.save()
        
        my_user = authenticate(request, email=get_email, password=get_password)  # Updated to use email
        
        if my_user is not None:

            login(request, my_user)
            messages.success(request, "User created & Login Success")
            return redirect('/')
        
    return render(request, "signup.html")


def handleLogin(request):
    if request.method == 'POST':
        get_email = request.POST.get("email")
        get_password = request.POST.get("pass")
        my_user = authenticate(request, email=get_email, password=get_password)  # Updated to use email
        if my_user is not None:
            login(request, my_user)
            messages.success(request, "Login Success")
            return redirect('/')
        else:
            messages.error(request, 'Incorrect Login Credentials')
            return redirect('/auth/login/')
    return render(request, "login.html")


def handleLogout(request):
    logout(request)
    messages.success(request, 'Logout success')
    return render(request, "home.html")

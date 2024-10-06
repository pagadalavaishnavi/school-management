from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def fun(request):
    return HttpResponse('<h1>i am working with the function 1</h1>')
def fun2(request,name):
    return HttpResponse(f'welcome to zenithyuga {name}')
def add(request,n1,n2):
    return HttpResponse(f'Addition of <br>{n1} and {n2} is {n1+n2}')
def add2(request):
    if request.GET and request.GET.get('n1') and request.GET.get('n2'):
        a=int(request.GET.get('n1'))
        b=int(request.GET.get('n2'))
        return HttpResponse(f'{a+b}')
    else:
        return HttpResponse("please tne values correctly")
def sub(request):
    d={'name':'manu','interns':['ram','seetha','hanuman','shiva','krish']}
    return render(request,'index.html',d)
def con(request):
    return render(request,'contact.html')

def abou(request):
    return render(request,'about.html')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import StudentProfile, FacultyProfile, AdminProfile

# Login View
def loginview(request, role=None):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        u = request.POST.get("usern")
        p = request.POST.get("passw")
        user = authenticate(request, username=u, password=p)
        if user is not None:
            # Check if the user has the role-specific profile
            if (role == 'student' and StudentProfile.objects.filter(user=user).exists()) or \
               (role == 'faculty' and FacultyProfile.objects.filter(user=user).exists()) or \
               (role == 'admin' and AdminProfile.objects.filter(user=user).exists()) or \
               (role is None):  # Default login with no specific role
                login(request, user)
                return redirect('profile')
            else:
                context = {'error': f'Invalid credentials for {role}'}
                return render(request, 'login.html', context)
        else:
            context = {'error': 'Invalid username and password'}
            return render(request, 'login.html', context)
    
    return render(request, 'login.html', {'role': role})

# Helper functions for registration validation
def userexit(x):
    return User.objects.filter(username=x).exists()

def length(y):
    return len(str(y)) > 8

def spaceexits(z):
    return len(z.split()) > 1

def isspl(a):
    return not a.isalnum()

def checkpass(b):
    return len(b) > 8

# Registration View
def register(request):
    if request.method == 'POST':
        u = request.POST.get("usern")
        f = request.POST.get("fname")
        l = request.POST.get("lname")
        m = request.POST.get("mail")
        p = request.POST.get("passw")
        phone = request.POST.get("phone")
        role = request.POST.get("role")

        # Validation checks
        if userexit(u):
            return render(request, 'register.html', {'warn': 'Username already exists'})
        if not length(u):
            return render(request, 'register.html', {'warn': 'Username should be of length > 8'})
        if spaceexits(u):
            return render(request, 'register.html', {'warn': 'Username should not contain spaces'})
        if not isspl(p):
            return render(request, 'register.html', {'warn': 'Password must contain special characters'})
        if not checkpass(p):
            return render(request, 'register.html', {'warn': 'Password should be of length > 8'})

        # Create user and assign to specific role
        user = User.objects.create_user(username=u, first_name=f, last_name=l, email=m, password=p)
        
        if role == 'student':
            StudentProfile.objects.create(user=user, email=m, phone_number=phone)
        elif role == 'faculty':
            FacultyProfile.objects.create(user=user, email=m, phone_number=phone)
        elif role == 'admin':
            AdminProfile.objects.create(user=user, email=m, phone_number=phone)
        
        return redirect('login')

    return render(request, 'register.html')

# Logout View
def LogoutView(request):
    logout(request)
    return redirect('login')

# Profile View
@login_required(login_url="login")
def profile(request):
    user = request.user
    user_details = None
    role = None

    # Check the role of the user
    if StudentProfile.objects.filter(user=user).exists():
        role = 'student'
        user_details = StudentProfile.objects.get(user=user)
    elif FacultyProfile.objects.filter(user=user).exists():
        role = 'faculty'
        user_details = FacultyProfile.objects.get(user=user)
    elif AdminProfile.objects.filter(user=user).exists():
        role = 'admin'
        user_details = AdminProfile.objects.get(user=user)
    
    context = {'user_details': user_details, 'role': role}
    return render(request, 'profile.html', context)

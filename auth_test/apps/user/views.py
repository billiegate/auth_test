from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import re

# Create your views here.
def home(request):
    # return HttpResponse('<h2>hello</h2>')
    return render(request, 'user/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            pass
        else:
            pass
    else:
        return render(request, 'user/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        errors = {}
        if re.match('[A-Z]{2}[a-z]*[0-9]{3}\W{2}', password) and len(password) > 16 :
            user = User.objects.create_user(username, email, password)
            user.save()
            user = authenticate(username=username, password=password)
        else:
            errors['password'] = 'password length must be more than 16 and should contain at least 2 uppercase letter 3 digits and 2 special character'
            return render(request, 'user/register.html', errors)

        if user: 
            return render(request, 'user/dashboard.html', errors)
        else:
            errors['user'] = 'unable to create user'
            return render(request, 'user/register.html', errors)

        
        
    else:
        return render(request, 'user/register.html')
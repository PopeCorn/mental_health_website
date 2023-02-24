from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        new_user = User.objects.create_user(username, email, pass1)
        new_user.save()
        messages.success(request, 'Your account has been succesfully created')
        return redirect('signin')

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return render(request, 'index.html', {'username': username})
        else:
            messages.error(request, 'That user does not exist')
            return redirect('http://127.0.0.1:8000/home')
        
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'Logged out succesfully')
    return redirect('home')
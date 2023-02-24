from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

def welcome(request):
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
        return redirect('login')

    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    pass
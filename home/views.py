from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def challenges(request):
    return render(request, 'challlenges.hml')

def quotes(request):
    return render(request, 'quotes.html')

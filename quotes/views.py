from django.shortcuts import render

def quotes(request):
    return render(request, 'quotes.html')
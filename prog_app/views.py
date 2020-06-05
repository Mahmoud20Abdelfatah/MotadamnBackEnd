from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def programe1(request):
    return render(request , 'development.html')

def programe2(request):
    return render(request ,'economic_support.html' )

def programe3(request):
    return render(request ,'medical.html' )

def programe4(request):
    return render(request ,'social_support.html' )

def programe5(request):
    return render(request ,'zakat.html' )

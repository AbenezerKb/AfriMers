from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'AfriMers/Home.html')

def about(request):
    return render(request, 'AfriMers/About.html')

def account(request):
    return render(request, 'AfriMers/Account.html')

def LogIn(request):
    return render(request, 'AfriMers/LogIn.html')

def Groceries(request):
    return render(request, 'AfriMers/Groceries.html')

def Purchase(request):
    return render(request, 'AfriMers/Purchase.html')



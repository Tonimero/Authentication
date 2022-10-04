from django.shortcuts import render, redirect

# Create your views here.

def login_app(request):
    return render (request, 'folder/login.html')
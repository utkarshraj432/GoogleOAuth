from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        messages.success(request, 'Login successful')
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

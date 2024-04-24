from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegistrationForm
from django.shortcuts import render

# Create your views here.

def my_view(request):
    return render(request, 'templates/home.html')

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.savee()

            return redirect("login")
        
    else:
        form = RegistrationForm()
    return render(request, "registration.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect("home")
        
def logout_view(request):
    logout(request)

    return redirect("login")
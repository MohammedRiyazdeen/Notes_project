from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login , logout 
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.


def register(request):  
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('list-note')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {"form":form})


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('list-note')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are successfully logged in as {username}!")
                return redirect('list-note')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {"form": form})


def LogoutPage(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect('login')

    return render(request, 'accounts/logout.html')
        












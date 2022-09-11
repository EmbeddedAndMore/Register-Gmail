from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout



class HomeView(View):

    def get(self, request):
        return render(request, 'accounts/home.html')


class UserRegisterView(View):
    def get(self, request):
        form = UserRegistrationForm
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            CustomUser.objects.create_user(**cd)
            messages.success(request, 'You Registered Successfully', 'success')
            return redirect('accounts:home')
        return render(request, 'accounts/register.html', {'form': form})


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully', 'success')
                return redirect('accounts:home')
            messages.error(request, 'Username or Password is Wrong', 'danger')
            return render(request, 'accounts/login.html', {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out Successfully', 'success')
        return redirect('accounts:home')


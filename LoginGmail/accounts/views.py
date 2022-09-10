from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
from django.contrib import messages
from .models import CustomUser


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
            #CustomUser.objects.create_user(cd['username'], cd['email'], cd['password'], cd['phone'])
            #print(list(cd))
            CustomUser.objects.create_user(**cd)
            messages.success(request, 'You Registered Successfully', 'success')
            return redirect('accounts:home')
        return render(request, 'accounts/register.html', {'form': form})



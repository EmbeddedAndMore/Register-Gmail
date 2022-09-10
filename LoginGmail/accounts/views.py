from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationForm


class HomeView(View):

    def get(self, request):
        return render(request, 'accounts/home.html')


class UserRegisterView(View):
    def get(self, request):
        form = UserRegistrationForm
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        pass

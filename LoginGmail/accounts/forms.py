from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('phone_number', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=11)

    # validations functions(email , Phone number)
    def clean_email(self):
        email = self.cleaned_data['email']
        user = CustomUser.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already exist')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone_number']
        user = CustomUser.objects.filter(phone_number=phone).exists()
        if user:
            raise ValidationError('this phone number is exist')
        return phone



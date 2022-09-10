from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.models import Group


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('email', 'phone_number')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', )}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)


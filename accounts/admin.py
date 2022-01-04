from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm 
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'date_of_joining', 'email', 'is_staff']
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('last_name',)}),
    # )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('first_name', 'last_name', 'date_of_joining',)}),)
    # )
    ordering = ('-date_of_joining',)

admin.site.register(CustomUser, CustomUserAdmin)


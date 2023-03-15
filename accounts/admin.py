from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form =  CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'phone_number', 'nat_id', 'email', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'nat_id', 'birth_date', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'nat_id', 'birth_date', )}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
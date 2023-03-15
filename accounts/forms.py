from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('phone_number', 'nat_id', 'birth_date', )
        # fields = ('password2', 'first_name', 'last_name', 'phone_number', 'birth_date', 'email', 'username', 'nat_id', 'password1', 'is_superuser', 'is_staff', 'is_active')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        
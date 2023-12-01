"""Core > forms > registration.py"""
# DJANGO IMPORTS
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Core.models import Seeker
USER_MODEL = get_user_model()


class SignupForm(UserCreationForm):
    """New user registration and signup form"""

    class Meta:
        """Meta class"""
        model = USER_MODEL
        fields = ('first_name', 'last_name', 'email', 'phone')



class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Seeker
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class LoginFormStep1(forms.Form):
    email = forms.EmailField()

class LoginFormStep2(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

"""Core > forms > __init__.py"""
from .registration import SignupForm, UserForm, LoginFormStep1, LoginFormStep2
from .user import UserUpdateForm, ProfileUpdateForm

# update the following list to allow classes to be available for import
# this is very useful especially when using from .file import *
__all__ = [SignupForm, UserUpdateForm, ProfileUpdateForm, UserForm, LoginFormStep1, LoginFormStep2 ]

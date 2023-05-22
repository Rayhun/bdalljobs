"""Core > views > __init__.py"""
from .index import IndexView
from .registration import SignupView, LoginView, Sign_upView

from .user import UserListView, UserDetailView, UserUpdateView, UserCreateView

# update the following list to allow classes to be available for import
# this is very useful especially when using from .file import *
# __all__ = [
#     IndexView, SignupView, LoginView, UserListView, UserDetailView,
#     UserUpdateView, UserCreateView,
# ]
__all__ = [
    IndexView, LoginView, UserListView, UserDetailView,
    UserUpdateView, UserCreateView, SignupView, Sign_upView
]

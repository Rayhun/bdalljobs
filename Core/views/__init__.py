"""Core > views > __init__.py"""
from .index import IndexView
from .registration import SignupView, LoginView, Sign_upView, create_user, login_step1, login_step2
from .profile import Profile

from .user import UserListView, UserDetailView, UserUpdateView, UserCreateView

# update the following list to allow classes to be available for import
# this is very useful especially when using from .file import *
# __all__ = [
#     IndexView, SignupView, LoginView, UserListView, UserDetailView,
#     UserUpdateView, UserCreateView,
# ]
__all__ = [
    IndexView, LoginView, UserListView, UserDetailView, Profile,
    UserUpdateView, UserCreateView, SignupView, Sign_upView, create_user, login_step1, login_step2
]

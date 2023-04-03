"""Core > models > __init__.py"""
from .user import User
from .profile import Profile
from .categories import Category
from .jobs import JobLevel, JobsPost, JobStatus

# update the following list to allow classes to be available for import
# this is very useful especially when using from .file import *
__all__ = [User, Profile, Category, JobStatus, JobLevel, JobsPost]

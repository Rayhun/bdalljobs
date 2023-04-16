"""API > urls.py"""
# DJANGO IMPORTS
from django.urls import path
# Local Import
from company import views

app_name = 'company'

urlpatterns = [
    path('profile/<int:pk>/', views.CompanyProfile.as_view(), name='profile'),
]

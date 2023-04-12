"""API > urls.py"""
# DJANGO IMPORTS
from django.urls import path
# Local Import
from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('details/<str:slug>/', views.JobDetailsView.as_view(), name='detail'),
    path('search/', views.JobSearchView.as_view(), name='search'),
]

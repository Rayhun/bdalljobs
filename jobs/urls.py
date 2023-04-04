"""API > urls.py"""
# DJANGO IMPORTS
from django.urls import path
# Local Import
from jobs import views

app_name = 'jobs'

urlpatterns = [
    # profile
    path('details/', views.JobDetailsView.as_view(),name='test'),
]

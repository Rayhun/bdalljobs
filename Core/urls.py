"""Core > urls.py"""
# DJANGO URLS
from django.urls import path
# CORE IMPORTS
from Core import views
from django.urls import path
from Core.views import create_user, login_step1, login_step2
app_name = 'core'

urlpatterns = [
    # index url ---------------------------------------------------------------
    path('', views.IndexView.as_view(), name='index'),

    # user --------------------------------------------------------------------
    path(
        'users/', views.UserListView.as_view(), name='users'
    ),
    path('profile/<int:pk>/', views.Profile.as_view(), name='profile'),
    path(
        'user/create/', views.UserCreateView.as_view(), name='user_create'
    ),
    path(
        'user/detail/<int:pk>',
        views.UserDetailView.as_view(),
        name='user_detail'
    ),
    path(
        'user/update/<int:pk>',
        views.UserUpdateView.as_view(),
        name='user_update'
    ),
    path('create/', create_user, name='create_user'),
    path('login_step1/', login_step1, name='login_step1'),
    path('login_step2/', login_step2, name='login_step2'),
]

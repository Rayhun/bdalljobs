"""Core > views > index.py"""
# PYTHON IMPORTS
import logging
from sys import _getframe
# DJANGO IMPORTS
from django.contrib import messages
from django.contrib.auth import get_user_model, views
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.translation import ugettext_lazy as _
# CORE IMPORTS
from Core.forms import SignupForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from Core.forms import UserForm, LoginFormStep1, LoginFormStep2
from Core.models import Seeker
from django.contrib.auth.hashers import make_password


logger = logging.getLogger(__name__)
USER_MODEL = get_user_model()


# - LoginView, LogoutView used from django.contrib.auth.views
# - PasswordResetView sends the mail
# - PasswordResetDoneView shows a success message for the above
# - PasswordResetConfirmView checks clicked link and prompts for a new password
# - PasswordResetCompleteView shows a success message for the above


def redirect_auth_users(request, message=None):
    """Redirect authenticated users to index view"""
    logger.debug(  # prints function name and description
        f"{_getframe().f_code.co_name} "
        f"Redirecting {request.user} to IndexView..."
    )
    if not message:  # default message
        message = _(f"{request.user}, you are redirected to Index page.")
    messages.info(request=request, message=message)
    return redirect(reverse_lazy('index'))


class SignupView(CreateView):
    """New user registration and signup view"""
    model = USER_MODEL
    form_class = SignupForm
    template_name = 'registration/signup.html'

    @staticmethod
    def get_redirect_message(request):
        """Returns a message to user when redirected"""
        return _(
            f"You are already registered as {request.user}. "
            f"Redirected you to Index page. "
            f"Please logout if you wish to create a new user."
        )

    def get(self, request, *args, **kwargs):
        """GET method"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"{request.user} is authenticated: {request.user.is_authenticated}"
        )
        # redirect authenticated users
        if request.user.is_authenticated:
            return redirect_auth_users(
                request=request, message=self.get_redirect_message(request)
            )

        # if user is not authenticated, proceed with SignupView
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """POST method"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Performing form validation..."
        )
        # redirect authenticated users
        if request.user.is_authenticated:
            return redirect_auth_users(
                request=request, message=self.get_redirect_message(request)
            )

        # if user is not authenticated, proceed with SignupView
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """form is clean and validated"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Form is clean and valid. Saving {form}"
        )
        self.object = form.save()
        self.object.refresh_from_db()  # creates profile instance via signals

        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"User account was created for {self.object}."
        )
        message = _(
            f"{self.object}, your user account was created successfully. "
            f"Please login using your email address and password."
        )
        messages.success(request=self.request, message=message)
        return redirect(reverse_lazy('login'))

    def form_invalid(self, form):
        """form is invalid"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Form is invalid. {form}"
        )
        logger.error(form.errors)  # log all form errors
        message = _("Validation error, please check all fields for any error.")
        messages.error(request=self.request, message=message)
        return super().form_invalid(form)


class Sign_upView(CreateView):
    """New user registration and signup view"""
    model = USER_MODEL
    form_class = SignupForm
    template_name = 'registration/sign_up.html'

    @staticmethod
    def get_redirect_message(request):
        """Returns a message to user when redirected"""
        return _(
            f"You are already registered as {request.user}. "
            f"Redirected you to Index page. "
            f"Please logout if you wish to create a new user."
        )

    def get(self, request, *args, **kwargs):
        """GET method"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"{request.user} is authenticated: {request.user.is_authenticated}"
        )
        # redirect authenticated users
        if request.user.is_authenticated:
            return redirect_auth_users(
                request=request, message=self.get_redirect_message(request)
            )

        # if user is not authenticated, proceed with SignupView
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """POST method"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Performing form validation..."
        )
        # redirect authenticated users
        if request.user.is_authenticated:
            return redirect_auth_users(
                request=request, message=self.get_redirect_message(request)
            )

        # if user is not authenticated, proceed with SignupView
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """form is clean and validated"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Form is clean and valid. Saving {form}"
        )
        self.object = form.save()
        self.object.refresh_from_db()  # creates profile instance via signals

        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"User account was created for {self.object}."
        )
        message = _(
            f"{self.object}, your user account was created successfully. "
            f"Please login using your email address and password."
        )
        messages.success(request=self.request, message=message)
        return redirect(reverse_lazy('login'))

    def form_invalid(self, form):
        """form is invalid"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Form is invalid. {form}"
        )
        logger.error(form.errors)  # log all form errors
        message = _("Validation error, please check all fields for any error.")
        messages.error(request=self.request, message=message)
        return super().form_invalid(form)


class LoginView(views.LoginView):
    """Overriding Django LoginView from django.contrib.auth.views"""

    @staticmethod
    def get_redirect_message(request):
        """Returns a message to user when redirected"""
        return _(
            f"You are already logged in as {request.user}. "
            f"Redirected you to Index page. "
            f"Please logout if you wish to log in as a new user."
        )

    def get(self, request, *args, **kwargs):
        """overriding GET method"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"{request.user} is authenticated: {request.user.is_authenticated}"
        )
        # redirect authenticated users
        if request.user.is_authenticated:
            return redirect_auth_users(
                request=request, message=self.get_redirect_message(request)
            )

        # if user is not authenticated, proceed with LoginView
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """overriding POST method"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Performing form validation..."
        )
        # redirect authenticated users
        if request.user.is_authenticated:
            return redirect_auth_users(
                request=request, message=self.get_redirect_message(request)
            )

        # if user is not authenticated, proceed with LoginView
        return super().post(request, *args, **kwargs)


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])

            user.save()
            return redirect('core:login_step1')
    else:
        form = UserForm()

    return render(request, 'registration/create_user.html', {'form': form})


def login_step1(request):
    if request.method == 'POST':
        form = LoginFormStep1(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = Seeker.objects.get(email=email)
            except Seeker.DoesNotExist:
                messages.error(request, 'Email not found. Please try again.')
                return redirect('core:login_step1')

            # Store user ID in session instead of the entire user instance
            request.session['user_id'] = user.user_id

            # Redirect to login_step2 page after successful email verification
            return redirect('core:login_step2')

    else:
        form = LoginFormStep1()

    return render(request, 'registration/login_step1.html', {'form': form})


def login_step2(request):
    user_id = request.session.get('user_id', None)

    if not user_id:
        return redirect('core:login_step1')

    try:
        user = Seeker.objects.get(user_id=user_id)
    except Seeker.DoesNotExist:
        # Handle the case where the user does not exist
        return redirect('core:login_step1')

    if request.method == 'POST':
        form = LoginFormStep2(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']

            # Use check_password to compare the entered password with the hashed password
            if check_password(password, user.password):
                return redirect('dashboard')
            else:
                messages.error(request, 'Incorrect password. Please try again.')

    else:
        form = LoginFormStep2()

    return render(request, 'registration/login_step2.html', {'email': user.email, 'form': form})


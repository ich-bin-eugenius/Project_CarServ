from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


class RegisterView(CreateView):
    """
    Handle the user registration process.

    This view uses Django's built-in `CreateView` to display and process the
    registration form. It uses the `RegisterForm` form class and renders the
    `register.html` template.

    After successful registration, the user is redirected to the homepage.

    Attributes:
        template_name (str): Path to the template used for rendering the registration page.
        form_class (Form): The form class used for user registration.
        success_url (str): The URL to redirect to after a successful registration.
    """

    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, 'Registration successful!')
        return super().form_valid(form)


class MyLoginView(LoginView):
    """
    A custom login view that renders a login page and redirects upon successful login.

    Attributes:
        template_name (str): Path to the login HTML template.

    Methods:
        get_success_url(): Determines the URL to redirect the user after a successful login.
    """

    template_name = 'login.html'

    def get_success_url(self):
        """
        Get the URL to redirect to after successful login.

        Returns:
            str: The URL to redirect to, either the 'next' parameter from the request or the root URL.
        """

        return self.request.GET.get('next', '/')


def user_logout(request):
    """
    Logs out the user and redirects to the homepage with a success message.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: A redirection to the homepage with a logout success message.
    """

    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home:home')

from django.http import HttpResponse
from django.shortcuts import render, redirect

# About
from .models import About

# Contact
from .models import ContactInfo
from .forms import MessageFromCustomerForm, SubscriberForm

# Home
from .models import Establishment

# Services
from .models import Service


# ------------About------------

def index(request) -> HttpResponse:
    """
    A view for the about page that displays information from the About model.

    This view gets all the About model objects that
    have the is_visible attribute set to True, and passes them in the context
    template 'about.html'.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with the rendered template 'about.html'.
    """

    about = About.objects.prefetch_related("features").first()
    return render(request, "apps/core/about.html", {"about": about})


# ------------Contact------------

def index(request):
    """
    A view for the contact page.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with the rendered template 'contact.html'.
    """

    if request.method == 'POST':
        form = MessageFromCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')

        context = {
            'message_form': form,
            'contacts': ContactInfo.objects.first()
        }
        return render(request, 'apps/core/contact.html', context=context)
    else:
        context = {
            'message_form': MessageFromCustomerForm(),
            'contacts': ContactInfo.objects.first()
        }
        return render(request, 'apps/core/contact.html', context=context)


def subscribe(request) -> HttpResponse:
    """
    A view for the subscribe page.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with the rendered template 'subscribe.html'.
    """

    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = SubscriberForm()

    return render(request, 'apps/core/subscribe.html', {'subscriber_form': form})


# ------------Home------------

def index(request) -> HttpResponse:
    """
    A view for the main page that displays information from the About model.

    This view gets all the Home model objects that
    have the is_visible attribute set to True, and passes them in the context
    template 'home.html'.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with the rendered template 'home.html'.
    """

    establishment = Establishment.objects.filter(is_visible=True)

    return render(request, 'apps/core/home.html', {'establishment': establishment})


# ------------Services------------

def index(request) -> HttpResponse:
    """
    A view for the service page that displays information from the Service model.

    This view gets all the Service model objects that
    have the is_visible attribute set to True and pass them in the context
    template 'service.html'.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with the rendered template 'service.html'.
    """

    services = Service.objects.filter(is_visible=True)
    return render(request, 'core/service.html', {'services': services})

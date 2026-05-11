from django.http import HttpResponse
from django.shortcuts import render, redirect

# About
from .models import About

# Contact
from .models import ContactInfo
from .forms import MessageFromCustomer, SubscriberForm
from django.contrib import messages

# Home
from .models import Establishment

# Services
from .models import Service


# ------------About------------

def index_about(request) -> HttpResponse:
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
    return render(request, "core/about.html", {"about": about})


# ------------Contact------------

def index_contact(request):
    """
    A view for the contact page.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with the rendered template 'contact.html'.
    """

    contact_info = ContactInfo.objects.first()
    all_messages = MessageFromCustomer.objects.all().order_by('-created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        msg_subject = request.POST.get('subject')
        msg_content = request.POST.get('message')

        if msg_content:
            new_msg = MessageFromCustomer(
                user=request.user,
                name=request.user.username,
                email=request.user.email,
                subject=msg_subject or "Feedback",
                message=msg_content
            )
            new_msg.save()

            messages.success(request, 'Thank you for your opinion! Everything went well.')
            return redirect('home:contact')

    context = {
        'contacts': contact_info,
        'reviews': all_messages,
    }
    return render(request, 'core/contact.html', context)


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

    return render(request, 'core/subscribe.html', {'subscriber_form': form})


# ------------Home------------

def index_home(request) -> HttpResponse:
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

    return render(request, 'core/home.html', {'establishment': establishment})


# ------------Services------------

def index_services(request) -> HttpResponse:
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

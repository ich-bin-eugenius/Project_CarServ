from django.http import HttpResponse
from django.shortcuts import render
from .models import Technicians, Testimonials


def index_404(request, exception=None) -> HttpResponse:
    """
    A view for the error page.


    This view simply displays the '404.html' template.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with rendered '404.html' template.
    """

    return render(request, 'pages/404.html', {'hide': True}, status=404)


def index_500(request) -> HttpResponse:
    """
    A view for the error page.


    This view simply displays the '500.html' template.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with rendered '500.html' template.
    """

    return render(request, 'pages/500.html', {'hide': True}, status=500)


def index_team(request) -> HttpResponse:
    """
    A view for the team page.

    This view simply displays the 'team.html' template.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with rendered 'team.html' template.
    """

    technicians = Technicians.objects.filter(is_visible=True).order_by('sort')
    context = {
        'technicians': technicians
    }
    return render(request, 'pages/team.html', context=context)


def index_testimonial(request) -> HttpResponse:
    """
    A view for the testimonial page.

    This view simply displays the 'testimonial.html' template.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with rendered 'testimonial.html' template.
    """
    testimonials = Testimonials.objects.filter(is_visible=True).order_by('sort')
    context = {
        'testimonials': testimonials
    }

    return render(request, 'pages/testimonial.html', context=context)

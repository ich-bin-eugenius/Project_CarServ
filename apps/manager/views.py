from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def is_manager(user) -> bool:
    """
    A view for the manager page.

    is designed to check whether the specified user belongs to a group named "manager".

    Args:
        user: The user whose groups are being checked.

    Returns:
    bool: True if the user belongs to the "manager" group, otherwise False.
    """

    return user.groups.filter(name='manager').exists()


@user_passes_test(is_manager, login_url='/login/')
def index(request) -> HttpResponse:
    return render(request, 'apps/manager.html')

from .models import ContactInfo, MessageFromCustomer
from .forms import SubscriberForm


def contacts(request):
    return {
        'subscriber_form': SubscriberForm(),
        'index_message': MessageFromCustomer.objects.first(),
        'index_contacts': ContactInfo.objects.first()
    }

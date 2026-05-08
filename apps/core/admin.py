from django.contrib import admin

# About
from .models import About, AboutFeature

# Contact
from .models import ContactInfo, MessageFromCustomer, Subscriber

# Home
from .models import Establishment

# Services
from .models import Service


# ------------About------------

class AboutFeatureInline(admin.TabularInline):
    model = AboutFeature
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_visible')
    list_filter = ('name', 'is_visible')
    search_fields = ('name', 'is_visible')


@admin.register(AboutFeature)
class AboutFeatureAdmin(admin.ModelAdmin):
    list_display = ('about', 'title', 'description')
    list_filter = ('order',)
    search_fields = ('description',)


# ------------Contact------------

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'is_visible')
    list_filter = ('is_visible', )
    list_editable = ('is_visible',)


@admin.register(MessageFromCustomer)
class MessageFromCustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'updated_at')
    list_filter = ('created_at', )
    list_editable = ('subject', 'email',)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', )
    list_editable = ('is_active',)


# ------------Home------------

@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'is_visible')
    list_filter = ('name', 'phone', 'email', 'is_visible')
    search_fields = ('name', 'address', 'phone', 'email', 'is_visible')


# ------------Services------------

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_visible')
    list_filter = ('is_visible', )
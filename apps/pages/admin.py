from django.contrib import admin
from .models import Technicians, Testimonials
from django.utils.safestring import mark_safe


@admin.register(Technicians)
class TechniciansAdmin(admin.ModelAdmin):
    list_display = ('photo_tag', 'name', 'is_visible', )
    list_filter = ('is_visible', )
    search_fields = ('name', )
    list_editable = ('name', 'is_visible', )

    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50"  height="50"/>')

    photo_tag.short_description = 'Photo'


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('photo_tag', 'name', 'is_visible')
    list_filter = ('is_visible', )
    search_fields = ('name', )
    list_editable = ('name', 'is_visible', )

    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50"  height="50"/>')

    photo_tag.short_description = 'Photo'

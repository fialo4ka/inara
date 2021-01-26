from django.http import HttpResponse
from django.urls import include, re_path, reverse
from django.utils.html import format_html

from django.contrib import admin

# Register your models here.
from .models import ArtWork

class ArtWorkAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    list_display = ('image_tag', 'name', 'art_type', 'column_number', 'art_status', 'price', 'year')

# Register the admin class with the associated model
admin.site.register(ArtWork, ArtWorkAdmin)

from django.http import HttpResponse
from django.urls import include, re_path, reverse
from django.utils.html import format_html

from django.contrib import admin

# Register your models here.
from .models import ArtWork

class ArtWorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'path', 'art_type', 'art_status', 'year', 'price')

# Register the admin class with the associated model
admin.site.register(ArtWork, ArtWorkAdmin)

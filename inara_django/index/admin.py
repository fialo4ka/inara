from django.contrib import admin

# Register your models here.
from .models import ArtWork

class ArtWorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'path', 'column_number', 'art_type', 'art_status', 'year', 'price')

# Register the admin class with the associated model
admin.site.register(ArtWork, ArtWorkAdmin)

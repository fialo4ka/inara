from django.db import models
from django.utils.html import mark_safe
from stdimage.models import StdImageField
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from stdimage.utils import render_variations

class ArtType(models.Model):
    name = models.CharField(max_length=50, help_text='Art type')

    def __str__(self):
        return self.name

class ArtStatus(models.Model):
    name = models.CharField(max_length=50, help_text='Art Status')

    def __str__(self):
        return self.name

class ColumnNumber(models.Model):
    name = models.CharField(max_length=1, help_text='Column Number')

    def __str__(self):
        return self.name


def image_processor(file_name, variations, storage):
    with storage.open(file_name) as f:
        with Image.open(f) as image:
            file_format = image.format

            # resize to a maximum of 1000x1000 keeping aspect ratio
            image.thumbnail((800, 800), resample=Image.ANTIALIAS)

            with BytesIO() as file_buffer:
                image.save(file_buffer, file_format)
                f = ContentFile(file_buffer.getvalue())
                # delete the original big image
                storage.delete(file_name)
                # save the resized version with the same filename and format
                storage.save(file_name, f)

    # render stdimage variations
    render_variations(file_name, variations, replace=True, storage=storage) 
    return False 

class ArtWork(models.Model):
    name = models.TextField(max_length=600, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    art_type = models.ForeignKey(ArtType, on_delete=models.RESTRICT, default=1, help_text='Select art type')
    art_status = models.ForeignKey(ArtStatus, default=1, on_delete=models.RESTRICT, help_text='Select art status')
    column_number = models.ForeignKey(ColumnNumber, default=1, on_delete=models.RESTRICT, help_text='Select art type', null=True, blank=True)
    photo = StdImageField(upload_to='artWorks', null=True, blank=True, render_variations=image_processor)
    sort = models.IntegerField(null=True, blank=True, default=1000)

    def __str__(self):
        return f'{self.name} {str(self.art_type)}'
    
    def image_tag(self):
        return mark_safe('<img src="/artWorks/%s" height="100" />' % (self.photo))
    


from django.db import models

# Create your models here.
class ArtWork(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=100)
    ART_TYPE = (
        ('P', 'PAINTINGS'),
        ('W', 'WATERCOLORS'),
        ('G', 'GRAPHICS'),
        ('D', 'DESIGN'),
    )
    STATE = (
        ('S', 'In private collection'),
        ('Fr', 'For Sale'),
    )
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.

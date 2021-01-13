from django.db import models

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

class ArtWork(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    size = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)
    art_type = models.ForeignKey(ArtType, on_delete=models.RESTRICT, default=1, help_text='Select art type')
    art_status = models.ForeignKey(ArtStatus, default=1, on_delete=models.RESTRICT, help_text='Select art status')
    column_number = models.ForeignKey(ColumnNumber, default=1, on_delete=models.RESTRICT, help_text='Select art type', null=True)

    def __str__(self):
        return f'{self.name} {str(self.art_type)}'



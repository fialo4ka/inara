# Generated by Django 3.1.5 on 2021-01-29 19:37

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20210129_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='sort',
            field=models.IntegerField(blank=True, default=1000, null=True),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='column_number',
            field=models.ForeignKey(blank=True, default=1, help_text='Select art type', null=True, on_delete=django.db.models.deletion.RESTRICT, to='index.columnnumber'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='name',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='photo',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='artWorks'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

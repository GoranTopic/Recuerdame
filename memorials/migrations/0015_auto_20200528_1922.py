# Generated by Django 3.0.6 on 2020-05-28 19:22

from django.db import migrations
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('memorials', '0014_auto_20200528_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memorial',
            name='pais',
            field=django_countries.fields.CountryField(blank=True, default=django.utils.timezone.now, max_length=746, multiple=True),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.0.6 on 2020-05-28 19:03

from django.db import migrations
import django_countries.fields
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('memorials', '0013_auto_20200521_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorial',
            name='pais',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='memorial',
            name='imagen_de_perfil',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=100, size=[1000, 1000], upload_to='profiles/'),
        ),
    ]
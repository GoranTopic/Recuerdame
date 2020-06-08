# Generated by Django 3.0.6 on 2020-05-30 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memorials', '0017_auto_20200530_2141'),
        ('eulogies', '0002_auto_20200530_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='eulogy',
            name='memorial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='eulogies', to='memorials.Memorial'),
            preserve_default=False,
        ),
    ]
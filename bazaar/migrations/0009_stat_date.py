# Generated by Django 2.1 on 2018-08-31 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0008_stat'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

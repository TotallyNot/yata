# Generated by Django 2.0.5 on 2018-11-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0018_auto_20181106_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='count',
            name='graph',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]

# Generated by Django 2.0.5 on 2018-11-08 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0019_count_graph'),
    ]

    operations = [
        migrations.AddField(
            model_name='count',
            name='watcher',
            field=models.FloatField(default=0),
        ),
    ]

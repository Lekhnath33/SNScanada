# Generated by Django 5.0.4 on 2024-04-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0002_alter_event_options_event_created_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
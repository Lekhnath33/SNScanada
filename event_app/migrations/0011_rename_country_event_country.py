# Generated by Django 5.0.4 on 2024-04-27 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0010_alter_event_postal_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Country',
            new_name='country',
        ),
    ]
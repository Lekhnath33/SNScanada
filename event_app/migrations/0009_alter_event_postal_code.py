# Generated by Django 5.0.4 on 2024-04-27 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0008_alter_event_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='postal_code',
            field=models.IntegerField(blank=True, default='1234', null=True),
        ),
    ]
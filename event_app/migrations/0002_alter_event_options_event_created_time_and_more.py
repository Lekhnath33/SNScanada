# Generated by Django 5.0.4 on 2024-04-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name_plural': 'Event'},
        ),
        migrations.AddField(
            model_name='event',
            name='created_time',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
        migrations.AlterModelTable(
            name='event',
            table='Event',
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-30 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0009_alter_vision_paragraph_alter_vision_paragraph_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vision',
            old_name='paragraph_title',
            new_name='content_title',
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-16 20:03

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0022_remove_term_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='term_content',
            field=tinymce.models.HTMLField(),
        ),
    ]

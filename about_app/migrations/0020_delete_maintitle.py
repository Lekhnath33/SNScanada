# Generated by Django 5.0.4 on 2024-04-30 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0019_remove_term_description_remove_term_main_title_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MainTitle',
        ),
    ]

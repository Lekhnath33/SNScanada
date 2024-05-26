# Generated by Django 5.0.4 on 2024-05-11 21:35

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_app', '0002_registrations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('participant_full_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=400)),
                ('province', models.CharField(max_length=400)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('your_contact', phonenumber_field.modelfields.PhoneNumberField(help_text='your contact number', max_length=13, region=None)),
                ('your_email', models.EmailField(max_length=254)),
                ('parents_full_name', models.CharField(max_length=200)),
                ('parents_contact', phonenumber_field.modelfields.PhoneNumberField(help_text='your contact number', max_length=13, region=None)),
                ('parents_email', models.EmailField(max_length=254)),
                ('program', models.CharField(choices=[('SUMMER', 'summer'), ('WINTER', 'winter')], max_length=12)),
                ('screenshot', models.ImageField(upload_to='uploads/')),
            ],
            options={
                'verbose_name_plural': 'Program Registration',
                'db_table': 'Program Registration',
            },
        ),
    ]

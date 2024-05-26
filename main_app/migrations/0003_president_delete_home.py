# Generated by Django 5.0.4 on 2024-04-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('p_message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'President',
                'db_table': 'President',
            },
        ),
        migrations.DeleteModel(
            name='Home',
        ),
    ]

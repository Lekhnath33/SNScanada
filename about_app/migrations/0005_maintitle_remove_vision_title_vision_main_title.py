# Generated by Django 5.0.4 on 2024-04-16 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0004_vision'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'MainTitle',
                'db_table': 'MainTitle',
            },
        ),
        migrations.RemoveField(
            model_name='vision',
            name='title',
        ),
        migrations.AddField(
            model_name='vision',
            name='main_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='about_app.maintitle'),
        ),
    ]
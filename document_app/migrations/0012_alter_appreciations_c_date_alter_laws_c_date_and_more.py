# Generated by Django 5.0.3 on 2024-05-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_app', '0011_alter_appreciations_c_date_alter_laws_c_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appreciations',
            name='c_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='laws',
            name='c_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='program_registrations',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='references',
            name='c_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='registrations',
            name='c_date',
            field=models.DateField(),
        ),
    ]
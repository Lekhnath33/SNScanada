# Generated by Django 5.0.4 on 2024-04-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('profile_pic', models.ImageField(upload_to='upload/')),
                ('position', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Committee',
                'db_table': 'Committee',
            },
        ),
        migrations.DeleteModel(
            name='Pcommittee',
        ),
        migrations.DeleteModel(
            name='Xcommittee',
        ),
    ]

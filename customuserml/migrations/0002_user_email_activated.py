# Generated by Django 5.0 on 2023-12-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuserml', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_activated',
            field=models.BooleanField(default=False, verbose_name='Email Activated'),
        ),
    ]

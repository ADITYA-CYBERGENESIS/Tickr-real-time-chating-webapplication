# Generated by Django 5.0 on 2023-12-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuserml', '0005_alter_user_email_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_token',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Email Token'),
        ),
    ]

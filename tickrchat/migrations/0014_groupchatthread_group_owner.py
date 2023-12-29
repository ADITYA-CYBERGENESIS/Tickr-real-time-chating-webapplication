# Generated by Django 5.0 on 2023-12-16 18:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickrchat', '0013_groupchatthread_groupbio'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchatthread',
            name='group_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Group_owner_user', to=settings.AUTH_USER_MODEL, verbose_name='GroupOwner'),
        ),
    ]
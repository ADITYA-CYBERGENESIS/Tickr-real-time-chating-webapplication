# Generated by Django 5.0 on 2023-12-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickrchat', '0003_remove_chatmessage_sent_time_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmessage',
            old_name='sent_time',
            new_name='sent_time_12',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='sent_time_24',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Time'),
        ),
    ]

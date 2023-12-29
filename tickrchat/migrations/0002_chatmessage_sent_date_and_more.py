# Generated by Django 5.0 on 2023-12-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickrchat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='sent_date',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='sent_time_date',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Time and date'),
        ),
    ]
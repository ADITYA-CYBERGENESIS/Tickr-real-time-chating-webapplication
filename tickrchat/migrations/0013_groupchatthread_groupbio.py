# Generated by Django 5.0 on 2023-12-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickrchat', '0012_alter_groupchatthread_groupuniqueid'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchatthread',
            name='Groupbio',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Group Bio'),
        ),
    ]
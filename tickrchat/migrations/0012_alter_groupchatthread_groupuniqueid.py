# Generated by Django 5.0 on 2023-12-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickrchat', '0011_alter_groupchatthread_groupuniqueid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupchatthread',
            name='groupuniqueid',
            field=models.CharField(blank=True, default=None, max_length=500, null=True, unique=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-12 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_remove_profile_ed_level_profile_job_zone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job_zone',
        ),
    ]

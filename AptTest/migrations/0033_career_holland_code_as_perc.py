# Generated by Django 4.2.1 on 2023-06-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AptTest', '0032_result_result_as_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='holland_code_as_perc',
            field=models.JSONField(default=dict),
        ),
    ]

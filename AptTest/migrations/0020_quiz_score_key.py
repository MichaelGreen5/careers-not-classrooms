# Generated by Django 4.2.1 on 2023-05-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AptTest', '0019_quiz_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='score_key',
            field=models.CharField(default=0, max_length=300),
        ),
    ]

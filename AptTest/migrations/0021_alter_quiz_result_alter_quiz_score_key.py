# Generated by Django 4.2.1 on 2023-05-26 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AptTest', '0020_quiz_score_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='result',
            field=models.JSONField(default=dict, max_length=300),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='score_key',
            field=models.JSONField(default=dict, max_length=300),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AptTest', '0014_quiz_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

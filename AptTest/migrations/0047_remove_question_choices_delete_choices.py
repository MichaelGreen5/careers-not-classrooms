# Generated by Django 4.2.1 on 2023-06-19 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AptTest', '0046_quiz_num_of_qs_left'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choices',
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
    ]

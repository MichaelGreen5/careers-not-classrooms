# Generated by Django 4.2.1 on 2023-05-27 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AptTest', '0024_alter_question_answer_delete_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AptTest', '0017_remove_question_answer_remove_quiz_result_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]

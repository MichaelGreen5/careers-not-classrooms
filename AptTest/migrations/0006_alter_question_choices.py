# Generated by Django 4.2.1 on 2023-05-24 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AptTest', '0005_question_quiz_delete_testmaster_delete_testquestion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.CharField(blank=True, choices=[('sd', 'Strongly Dislike'), ('d', 'Dislike'), ('u', 'Unsure'), ('l', 'Like'), ('sl', 'Strongly Like')], max_length=150),
        ),
    ]

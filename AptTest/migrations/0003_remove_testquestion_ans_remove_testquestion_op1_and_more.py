# Generated by Django 4.2.1 on 2023-05-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AptTest', '0002_career_holland_code_userprofile_a_score_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testquestion',
            name='ans',
        ),
        migrations.RemoveField(
            model_name='testquestion',
            name='op1',
        ),
        migrations.RemoveField(
            model_name='testquestion',
            name='op2',
        ),
        migrations.RemoveField(
            model_name='testquestion',
            name='op3',
        ),
        migrations.RemoveField(
            model_name='testquestion',
            name='op4',
        ),
        migrations.AddField(
            model_name='testquestion',
            name='answers',
            field=models.IntegerField(blank=True, choices=[(-10, 'Strongly Dislike'), (-5, 'Dislike'), (0, 'Unsure'), (5, 'Like'), (10, 'Strongly Like')], default=0),
        ),
    ]

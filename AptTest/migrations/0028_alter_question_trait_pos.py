# Generated by Django 4.2.1 on 2023-05-30 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AptTest', '0027_remove_quiz_completed_remove_quiz_result_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='trait_pos',
            field=models.CharField(max_length=350, null=True),
        ),
    ]

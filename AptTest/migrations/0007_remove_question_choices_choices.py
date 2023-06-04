# Generated by Django 4.2.1 on 2023-05-24 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AptTest', '0006_alter_question_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choices',
        ),
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ch1', models.CharField(max_length=200, null=True)),
                ('ch2', models.CharField(max_length=200, null=True)),
                ('ch3', models.CharField(max_length=200, null=True)),
                ('ch4', models.CharField(max_length=200, null=True)),
                ('ch5', models.CharField(max_length=200, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AptTest.question')),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-13 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AptTest', '0040_question_json_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='job_zone',
            field=models.IntegerField(blank=True, choices=[(1, 'Some High School'), (2, 'High School Diploma or GED'), (3, "Associate's Degree or Vocational School"), (4, "Bachelor's Degree"), (5, "Master's Degree or Higher")], default=1),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AptTest.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

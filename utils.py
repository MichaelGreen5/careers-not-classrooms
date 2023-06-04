# set career holland code scores as percents
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LaunchPad.settings')
django.setup()

from AptTest.models import Career, holland_json_as_percent

all_careers = Career.objects.all()
for obj in all_careers:
    obj.holland_code_as_perc = holland_json_as_percent(obj.holland_code_scores.items())
    obj.save()

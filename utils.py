# set career holland code scores as percents
import os
import django
import json
import pyexcel as pe
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LaunchPad.settings')
django.setup()

def set_career_data_perc():
    from AptTest.models import Career, holland_json_as_percent

    all_careers = Career.objects.all()
    for obj in all_careers:
        obj.holland_code_as_perc = holland_json_as_percent(obj.holland_code_scores.items())
        obj.save()







def remove_data_from_sheet():
   

    data = pe.get_records(file_name='jobs_by_holland_code.ods')
    keywords = ['First Interest High-Point', 'Second Interest High-Point', 'Third Interest High-Point']
    rows_to_delete = []


    for i in range(len(data) - 1, -1, -1):
        row = data[i]
        for value in row.values():
            if any(keyword in str(value) for keyword in keywords):
                rows_to_delete.append(i)
                break  

    for row_index in rows_to_delete:
        del data[row_index]

    pe.save_as(records=data, dest_file_name='jobs_by_holland_modified.ods')

# takes spreadsheet data and formats into ('job_title', holland_code_json_data)
def holland_jobs_to_json():
    data = pe.get_records(file_name='jobs_by_holland_modified.ods')
    db_data = []
    for i in range(0, len(data), 6):
        rows = data[i:i+6]
        career_data_dict = {}
        for row in rows:
            each_row = list(row.items())
            job_title = each_row[0]
            key = each_row[1]
            value = each_row[2]
            career_data_dict[key[1]] = value[1]
            title = job_title[1]
        job_data_tup = (title, json.dumps(career_data_dict))
        db_data.append(job_data_tup)

    return db_data

        


def load_data(career_db_data):
    from AptTest.models import Career
    
    for tup in career_db_data:
        career_keys = ['name', 'holland_code_scores']
        json_data = json.loads(tup[1])
        career_values = [tup[0], json_data]
        career_data = dict(zip(career_keys,career_values ))
      
        career_obj = Career(**career_data)
        career_obj.save()

data = holland_jobs_to_json()

load_data(data)
set_career_data_perc()

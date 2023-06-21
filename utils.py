# set career holland code scores as percents
import os
import django
import json
import pyexcel as pe
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LaunchPad.settings')
django.setup()

def set_career_data_perc():
    from AptTest.models import Career, json_as_percent

    all_careers = Career.objects.all()
    for obj in all_careers:
        obj.work_activities_as_perc = json_as_percent(obj.work_activities.items())
        obj.save()

set_career_data_perc()





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

    pe.save_as(records=data, dest_file_name='jobs_by_holland_onet_id.ods')


def delete_every_other_row(filename):
    data = pe.get_records(file_name=filename)
    for i in range(len(data)-1, -1, -2):
        del data[i]
    pe.save_as(records=data, dest_file_name='work_activities.modified.ods')
        



# takes spreadsheet data and formats into ('job_title', json_data)
def job_sheet_to_json(filename, sheet_rows_per_obj, job_name_col_num, key_col_num, value_col_num):
    data = pe.get_records(file_name=filename)
    db_data = []
    for i in range(0, len(data), sheet_rows_per_obj):
        rows = data[i:i+sheet_rows_per_obj]
        career_data_dict = {}
        for row in rows:
            each_row = list(row.items())
            job_name = each_row[job_name_col_num-1]
            key = each_row[key_col_num-1]
            value = each_row[value_col_num-1]
            career_data_dict[key[1]] = value[1]
            name = job_name[1]
        job_data_tup = (name, json.dumps(career_data_dict))
        db_data.append(job_data_tup)
    
    return db_data




def load_data_to_career(career_db_data):
    from AptTest.models import Career
    
    for tup in career_db_data:
        career_keys = ['name', 'holland_code_scores']
        json_data = json.loads(tup[1])
        career_values = [tup[0], json_data]
        career_data = dict(zip(career_keys,career_values ))
      
        career_obj = Career(**career_data)
        career_obj.save()


# load_data(data)
# set_career_data_perc()
# remove_data_from_sheet()


def get_rows_by_job_name (filename, data_row_start, name_col_num,  target_col_num):
    out_data = []
    sheet = pe.get_sheet(file_name=filename)
    for i in range(data_row_start, len(sheet)):
        row = sheet.row[i]
        job_name, data_point = row[name_col_num-1], row[target_col_num-1]
        out_data.append((job_name, data_point))
    return out_data
                   


def add_column_to_career(data):
    from AptTest.models import Career
    all_careers = Career.objects.all()
    
    for career in all_careers:
        for i in data:
            if i[0] == career.name:
                career.work_activities = json.loads(i[1])
                career.save()

        
        

# data = job_sheet_to_json('work_activities.modified.ods', 41, 2, 4, 7)


# add_column_to_career(data)
from AptTest.models import Result
def set_work_activities(result_obj):
    out_dict = {}
    json_obj = result_obj.work_activities
    
    for key, value in json_obj.items():
        out_dict[key] = 2.5
    result_obj.work_activities = out_dict
    result_obj.save()
        
    


# result_obj = Result.objects.get(pk=2)
# set_work_activities(result_obj)
        
    




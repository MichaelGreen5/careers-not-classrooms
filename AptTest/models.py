from django.db import models
from django.contrib.auth.models import User
import json

HOLLAND_CODE_CHOICES = [
    'Realistic',
    'Investigative',
    'Artistic',
    'Social',
    'Enterprising',
    'Conventional'

]

WORK_ACTIVITIES = [
    'Getting Information', 'Thinking Creatively', 'Processing Information', 'Working with Computers', 
    'Handling and Moving Objects', 'Training and Teaching Others', 'Analyzing Data or Information', 
    'Developing and Building Teams', 'Selling or Influencing Others', 'Staffing Organizational Units',
    'Coaching and Developing Others', 'Scheduling Work and Activities', 'Assisting and Caring for Others',
    'Documenting/Recording Information', 'Controlling Machines and Processes', 'Developing Objectives and Strategies',
    'Monitoring and Controlling Resources', 'Performing Administrative Activities', 'Making Decisions and Solving Problems', 
    'Updating and Using Relevant Knowledge', 'Performing General Physical Activities', 'Identifying Objects, Actions, and Events', 
    'Organizing, Planning, and Prioritizing Work', 'Providing Consultation and Advice to Others', 'Coordinating the Work and Activities of Others', 
    'Inspecting Equipment, Structures, or Materials', 'Repairing and Maintaining Electronic Equipment', 'Repairing and Maintaining Mechanical Equipment', 
    'Guiding, Directing, and Motivating Subordinates', 'Resolving Conflicts and Negotiating with Others', 'Monitoring Processes, Materials, or Surroundings',
    'Communicating with People Outside the Organization', 'Interpreting the Meaning of Information for Others', 
    'Performing for or Working Directly with the Public', 'Operating Vehicles, Mechanized Devices, or Equipment',
    'Judging the Qualities of Objects, Services, or People', 'Communicating with Supervisors, Peers, or Subordinates',
    'Establishing and Maintaining Interpersonal Relationships', 'valuating Information to Determine Compliance with Standards',
    'Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment', 'Estimating the Quantifiable Characteristics of Products, Events, or Information'

]

INTEREST_LEVEL = [
    (-2, 'Strongly Dislike'),
    (-1, 'Dislike'),
    (0, 'Unsure'),
    (1, 'Like'),
    (2, 'Strongly Like')
]
QUESTION_TYPES = [
     (1, 'Holland Code'),
    (2, 'Job Zone'),
    (3, 'Work Activities'),
    (4, 'General Skills'),
    
    
]


JOB_ZONE_CHOICES = [
      (1,"Some High School"),
      (2, "High School Diploma or GED"),
      (3, "Associate's Degree or Vocational School"),
      (4, "Bachelor's Degree"), 
      (5, "Master's Degree or Higher")
    ]

def json_as_percent(json_obj):
        result_as_perc = {}
        total_value = 0
        for key, value in json_obj:
            total_value += value
           
        for key, value in json_obj:
            result_as_perc[key] = round((value/total_value) * 100, 2)
       
        return result_as_perc

def get_top_results(input_data_dict, num_of_results):
        sorted_data =  dict(sorted(input_data_dict.items(), key=lambda x: x[1], reverse=True))
        top_traits_list= list(sorted_data.items())[:num_of_results]
        top_traits = [trait[0] for trait in top_traits_list]
        return top_traits

class Career(models.Model):
    name = models.CharField(max_length=256, null= True)
    holland_code_scores= models.JSONField(default=dict)
    holland_code_as_perc = models.JSONField(default=dict)
    job_zone = models.IntegerField(default=0)
    work_activities= models.JSONField(default=dict)
    work_activities_as_perc = models.JSONField(default=dict)
    


    def __str__(self):
        return self.name
    
    def holland_code_perc(self):
        return json_as_percent(self.holland_code_scores.items())
    
    
    def get_top_two_holland(self):
        return get_top_results(self.holland_code_as_perc, 2)
      
    
    def get_top_five_work_activites(self):
        return get_top_results(self.work_activities_as_perc, 5)
   

    

    
    


    
    




class Question(models.Model):
    question = models.CharField(max_length=200,null=True)
    json_choices = models.JSONField(default=dict, )
    trait_pos = models.CharField(max_length=350, null= True)
    question_type = models.IntegerField(choices=QUESTION_TYPES, default=1)
   
    
    
    
    def __str__(self):
        return self.question
    
    
    

    def score_ans(self, answer_obj, CHOICES):
            pts = int(answer_obj.answer)
            ans = ('', pts)
            if '-' in self.trait_pos:
                trait_pos_list = self.trait_pos.split("-")
            else:
                trait_pos_list = self.trait_pos
            traits = []
            for value in CHOICES:
                if value in trait_pos_list:
                    traits.append(value)

                    ans = (traits, pts)
            
            return ans




class Quiz(models.Model):
    name = models.CharField(max_length=256, default= 'quiz')
    user = models.ForeignKey(User, default= 1, on_delete= models.CASCADE)
    questions = models.ManyToManyField('Question', related_name= 'quiz_questions')
    starter_questions = models.ManyToManyField('Question', related_name= 'starter_questions')
    num_of_qs_left = models.IntegerField(default=10)
    score_key = models.JSONField(default=dict)
   
    

    def __str__(self):
        return self.name + ' for ' + str(self.user)
    #TODO make this work
    def generate_question(self):
        return [2,4,6,8]


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    answer = models.TextField(max_length= 256, null = True, default = 0)

    def __str__(self):
        return str(self.user) + " answer to " + str(self.question)



    
    
class Result(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete= models.CASCADE)
    holland_result = models.JSONField(default=dict)
    holland_result_as_percent = models.JSONField(default=dict)
    job_zone = models.IntegerField(choices= JOB_ZONE_CHOICES, blank = True, default = 1)
    work_activities = models.JSONField(default= dict)
    work_activities_as_percent = models.JSONField(default=dict)
    questions_asked = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)


    def calc_holland_result_percent(self):
        return json_as_percent(self.holland_result.items())
    
    def calc_work_result_percent(self):
        return json_as_percent(self.work_activities.items())
    
    #TODO use top results to better match
    def career_match(self, all_careers):
        career_match_list = [] # list of tuples(career obj, avg% match to user result)
       
        
        for obj in all_careers:
            holland_result_dict = self.holland_result_as_percent
            holland_career_dict = obj.holland_code_as_perc

            work_act_result_dict = self.work_activities_as_percent
            work_act_career_dict = obj.work_activities_as_perc
            
            holland_common_keys = set(holland_result_dict.keys()) & set(holland_career_dict.keys())
            
    
            work_act_common_keys = set(work_act_result_dict.keys()) & set(work_act_career_dict.keys())

            all_common_keys = holland_common_keys.union(work_act_common_keys)
            
            combined_result_dict = work_act_result_dict | holland_result_dict
            combined_career_dict = work_act_career_dict | holland_career_dict
            
            
            
            percent_diff_dict = {}
            
           
            
            for key in all_common_keys:
                v1 = combined_result_dict[key]
                v2 = combined_career_dict[key]

                diff = v2-v1
                perc_diff = (diff/v1) * 100
                percent_diff_dict[key] = perc_diff

      
            
            all_percents = 0

           
            for v in percent_diff_dict.values():
                all_percents += abs(v)
                avg_perc_diff = all_percents / len(percent_diff_dict)
                
                

            career_obj, user_avg_perc_match = obj, abs(avg_perc_diff-100)
            career_match_list.append((career_obj, round(user_avg_perc_match, 2)))

        
        return career_match_list


            


   
        
       





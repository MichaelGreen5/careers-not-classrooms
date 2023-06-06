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

INTEREST_LEVEL = [
    (-2, 'Strongly Dislike'),
    (-1, 'Dislike'),
    (0, 'Unsure'),
    (1, 'Like'),
    (2, 'Strongly Like')
]

def holland_json_as_percent(json_obj):
        result_as_perc = {}
        total_value = 0
        for key, value in json_obj:
            total_value += value
           
        for key, value in json_obj:
            result_as_perc[key] = round((value/total_value) * 100, 2)
       
        return result_as_perc

class Career(models.Model):
    name = models.CharField(max_length=256, null= True)
    holland_code_scores= models.JSONField(default=dict)
    holland_code_as_perc = models.JSONField(default=dict)
    


    def __str__(self):
        return self.name
    
    def holland_code_perc(self):
        return holland_json_as_percent(self.holland_code_scores.items())
    



class Choices(models.Model):
    ch1 = models.CharField(max_length=200,null=True)
    ch2 = models.CharField(max_length=200,null=True)
    ch3 = models.CharField(max_length=200,null=True)
    ch4 = models.CharField(max_length=200,null=True)
    ch5 = models.CharField(max_length=200,null=True)
    ch6 = models.CharField(max_length=200,null=True)


class Question(models.Model):
    question = models.CharField(max_length=200,null=True)
    choices = models.ForeignKey(Choices, on_delete= models.CASCADE, null= True)
    trait_pos = models.CharField(max_length=350, null= True)
   
    
    
    
    def __str__(self):
        return self.question
    
    def score_ans(self, user_answer):
        pts = 0
        ans = ('Realistic', pts)
        for key in INTEREST_LEVEL:
            if key[1] == user_answer:
                pts = key[0]
        #some trait_pos have two traits seperated by -
        if '-' in self.trait_pos:
            trait_pos_list = self.trait_pos.split("-")
        else:
            trait_pos_list = self.trait_pos
        
        traits = []       
        for k in HOLLAND_CODE_CHOICES:
            if k in trait_pos_list:
                traits.append(k)     
        ans= (traits, pts)  
        return ans
        



    







class Quiz(models.Model):
    name = models.CharField(max_length=256, default= 'quiz')
    questions = models.ManyToManyField('Question', related_name= 'quiz_questions')
    score_key = models.JSONField(default=dict)
   
    

    def __str__(self):
        return self.name
    
    # ensures quiz results do not include negative numbers and are scaled accurately 
    def scale_results(self):
        pass

    
    
class Result(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete= models.CASCADE)
    result = models.JSONField(default=dict)
    result_as_percent = models.JSONField(default=dict)
    completed = models.BooleanField(default=False)


    def calc_result_percent(self):
        return holland_json_as_percent(self.result.items())
    

    def career_match(self, all_careers):
        career_match_list = [] # list of tuples(career obj, avg% match to user result)
        for obj in all_careers:
            result_dict = self.result_as_percent
            career_dict = obj.holland_code_as_perc
            common_keys = set(result_dict.keys()) & set(career_dict.keys())
            percent_diff_dict = {}
            
            for key in common_keys:
                v1 = result_dict[key]
                v2 = career_dict[key]

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


            


   
        
       





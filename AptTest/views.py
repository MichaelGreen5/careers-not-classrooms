from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView

from AptTest.models import Question, Quiz, Result, Career, Answer
def start_quiz(request):
    SCORE_KEY = {"Realistic": 20, "Investigative": 20, "Artistic": 20, "Social": 20, "Enterprising": 20, "Conventional": 20}
    WORK_ACTIVITIES = {"Getting Information": 2.5, "Thinking Creatively": 2.5, "Processing Information": 2.5, "Working with Computers": 2.5, "Handling and Moving Objects": 2.5, "Training and Teaching Others": 2.5, "Analyzing Data or Information": 2.5, "Developing and Building Teams": 2.5, "Selling or Influencing Others": 2.5, "Staffing Organizational Units": 2.5, "Coaching and Developing Others": 2.5, "Scheduling Work and Activities": 2.5, "Assisting and Caring for Others": 2.5, "Documenting/Recording Information": 2.5, "Controlling Machines and Processes": 2.5, "Developing Objectives and Strategies": 2.5, "Monitoring and Controlling Resources": 2.5, "Performing Administrative Activities": 2.5, "Making Decisions and Solving Problems": 2.5, "Updating and Using Relevant Knowledge": 2.5, "Performing General Physical Activities": 2.5, "Identifying Objects, Actions, and Events": 2.5, "Organizing, Planning, and Prioritizing Work": 2.5, "Providing Consultation and Advice to Others": 2.5, "Coordinating the Work and Activities of Others": 2.5, "Inspecting Equipment, Structures, or Materials": 2.5, "Repairing and Maintaining Electronic Equipment": 2.5, "Repairing and Maintaining Mechanical Equipment": 2.5, "Guiding, Directing, and Motivating Subordinates": 2.5, "Resolving Conflicts and Negotiating with Others": 2.5, "Monitoring Processes, Materials, or Surroundings": 2.5, "Communicating with People Outside the Organization": 2.5, "Interpreting the Meaning of Information for Others": 2.5, "Performing for or Working Directly with the Public": 2.5, "Operating Vehicles, Mechanized Devices, or Equipment": 2.5, "Judging the Qualities of Objects, Services, or People": 2.5, "Communicating with Supervisors, Peers, or Subordinates": 2.5, "Establishing and Maintaining Interpersonal Relationships": 2.5, "Evaluating Information to Determine Compliance with Standards": 2.5, "Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment": 2.5, "Estimating the Quantifiable Characteristics of Products, Events, or Information": 2.5}
    quiz, created = Quiz.objects.get_or_create(user=request.user)
    result, created = Result.objects.get_or_create(user= request.user, quiz= quiz)
    result.holland_result = SCORE_KEY
    result.work_activities = WORK_ACTIVITIES
    result.questions_asked = 0
    result.holland_result_as_percent = result.calc_holland_result_percent()
    result.work_activities_as_percent = result.calc_work_result_percent()
    result.save()
    return redirect('AptTest:question', pk=15)

#TODO this should be more flexible. serve up questions based on question type. smart questions to ask good info only. different every time. answer should be saved in question?
def first_question_view(request, pk):

    quiz, created = Quiz.objects.get_or_create(user=request.user)
    # question = quiz.questions.get(id=15)
    question = Question.objects.get(pk=pk)
    
    result, created = Result.objects.get_or_create(user= request.user, quiz= quiz)
   
   
    choices = dict(sorted(question.json_choices.items(), key=lambda x: x[1]))

    context = {'quiz':quiz, 'question': question, 'choices':choices}
    if request.method == 'POST':
        
        answer, created = Answer.objects.get_or_create(user= request.user, question = question)
        user_answer = request.POST.get('select ' + str(question.pk))
        print(user_answer)

        answer.answer = user_answer
        answer.save()
        
       
       
        # result.job_zone = user_answer


        
        # result.save()
     
        #TODO dynamically generate questoin pk
        # return redirect('model_detail', pk=random_pk)
        return redirect('AptTest:apt_test')
    else:
        
        return render(request, 'first_questions.html', context )


def work_activitity_questions(request, pk):
    quiz, created = Quiz.objects.get_or_create(user=request.user)
    question = Question.objects.get(pk=pk)
    choices = dict(sorted(question.json_choices.items(), key=lambda x: x[1]))
    

def questions(request, pk):
    quiz, created = Quiz.objects.get_or_create(user=request.user)
    question = Question.objects.get(pk=pk)
    choices = dict(sorted(question.json_choices.items(), key=lambda x: x[1]))
    if request.method == 'POST':
        result, created = Result.objects.get_or_create(user= request.user, quiz= quiz)
       
        answer_obj,created = Answer.objects.get_or_create(user=request.user, question=question)
        user_answer = request.POST.get('vbtn-radio')
        answer_obj.answer = user_answer
        answer_obj.save()
        if question.question_type == 1:
            answer=question.score_holland_ans(answer_obj)
                
            if len(answer[0]) > 1:
                for trait in answer[0]:
                    result.holland_result[trait] += answer[1] 
            else:
                trait = ''.join(answer[0])
                result.holland_result[trait] += answer[1]

            
            result.holland_result_as_percent = result.calc_holland_result_percent()
        elif question.question_type == 2:
            result.job_zone = answer_obj.answer
            
        elif question.question_type == 3:
            
            answer = question.score_work_act_ans(answer_obj)
            result.work_activities[answer[0]] += answer[1]
            result.work_activities_as_percent = result.calc_work_result_percent()
            
        result.questions_asked += 1
        result.save()
        
        return redirect('AptTest:question', pk=pk+1)
        # return redirect('AptTest:results', pk=int(quiz.pk))
    else:
        # if quiz.completed:
        #     return render(request, 'quiz_complete.html', {'quiz':quiz,})
        # else:
        return render(request, 'multi_select_question.html', {'quiz':quiz, 'question': question, 'choices':choices})

def apt_results(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    
  
    result = Result.objects.get(user= request.user, quiz= quiz)
    zone_careers = Career.objects.filter(job_zone__lte = result.job_zone)
    job_match_data = result.career_match(zone_careers)
    sorted_job_match_data = sorted(job_match_data, key = lambda x: x[1], reverse=True)
    best_matches = sorted_job_match_data[:20]

    #match result with carrers





    
    return render(request, 'apt_results.html',{'quiz':quiz, 'result': result, 'best_matches' :best_matches})




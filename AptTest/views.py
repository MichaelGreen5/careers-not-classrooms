from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView

from AptTest.models import Question, Quiz, Result, Career

def first_questions(request):
    quiz = Quiz.objects.get(name= 'Apt Test')
    question = quiz.questions.get(id=15)
    choices = question.json_choices

    if request.method == 'POST':
         result, created = Result.objects.get_or_create(user= request.user, quiz= quiz)
         user_answer = request.POST.get('select ' + str(question.pk))
         result.job_zone = user_answer
         result.save()
         return redirect('AptTest:apt_test')
    else:
        return render(request, 'first_questions.html', {'quiz':quiz, 'question': question, 'choices':choices})

def apt_test(request):
    SCORE_KEY = {"Realistic": 20, "Investigative": 20, "Artistic": 20, "Social": 20, "Enterprising": 20, "Conventional": 20}
    quiz = Quiz.objects.get(name= 'Apt Test')
    questions = quiz.questions.filter(question_type = 1)
    if request.method == 'POST':
        result, created = Result.objects.get_or_create(user= request.user, quiz= quiz)
        result.holland_result = SCORE_KEY
        result.save()
        for q in questions:
            name = 'vbtn-radio ' + str(q.pk)
            user_answer = request.POST.get(name)
            answer=q.score_ans(user_answer)
            
            if len(answer[0]) > 1:
               for trait in answer[0]:
                   result.holland_result[trait] += answer[1] 
            else:
                trait = ''.join(answer[0])
                result.holland_result[trait] += answer[1]

            result.save()
        
        result.holland_result_as_percent = result.calc_result_percent()
        result.save()
        quiz.completed = True
        quiz.save()

        return redirect('AptTest:results', pk=int(quiz.pk))
    else:
        # if quiz.completed:
        #     return render(request, 'quiz_complete.html', {'quiz':quiz,})
        # else:
        return render(request, 'apt_test.html', {'quiz':quiz, 'questions': questions})

def apt_results(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    careers = Career.objects.all()
  
    result = Result.objects.get(user= request.user, quiz= quiz)
    job_match_data = result.career_match(careers)
    sorted_job_match_data = sorted(job_match_data, key = lambda x: x[1], reverse=True)
    best_matches = sorted_job_match_data[:20]

    #match result with carrers





    
    return render(request, 'apt_results.html',{'quiz':quiz, 'result': result, 'best_matches' :best_matches})




from typing import List
from django.shortcuts import render
from django.views.generic import ListView 
from django.http import JsonResponse

from .models import Quiz
from questions.models import Answer, Question
from results.models import Result


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/home.html'
    context_object_name = 'quiz_list'
    

def about_view(request, *args, **kwargs):
    return render(request, 'quizes/about_page.html')

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {'quiz_obj': quiz})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions_and_answers = []

    # get all the questions
    for que in quiz.get_questions():
        answers = []
        # append all the ans of the que to the ans list
        for ans in que.get_answers():
            answers.append(ans.answer_text)
        questions_and_answers.append({que.question_text: answers})

    return JsonResponse({
        'data': questions_and_answers,
        'duration': quiz.duration
    })

def save_quiz_view(request, pk):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax:
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for q in data_.keys():
            question = Question.objects.get(question_text=q)
            questions.append(question)
        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.no_of_questions
        results = []
        correct_answer = None

        for que in questions:
            ans_selected = request.POST.get(que.question_text)
            if ans_selected != '':
                question_answers = Answer.objects.filter(question=que)
                for ans in question_answers:
                    if ans_selected == ans.answer_text:
                        if ans.is_correct:
                            score += 1
                            correct_answer = ans.answer_text
                            # break
                    else:
                        if ans.is_correct:
                            correct_answer = ans.answer_text
                
                results.append({que.question_text: {'correct_answer': correct_answer, 'answered': ans_selected}})
            else:
                results.append({que.question_text: 'not answered'})
        score_ = (score / quiz.no_of_questions) * 100
        Result.objects.create(quiz=quiz, user=user, attempts=1, score=score_)

        if score_ >= quiz.req_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results })        



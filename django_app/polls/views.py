from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # question_id 가 pk인 Question 객체를 가저와
    # context라는 이름을 가진 dict에 'question'이라는 키 값으로 위 변수를 할당
    # 이 후 'polls/detail.html'과 context를 랜더한 결과를 리턴
    try:
        question =  Question.objects.get(pk = question_id)
    except Question.DoesNotExist as e:
        raise Http404('Question does not exist')
    context = {
        'question':question,
    }
    return render(request, 'polls/detail.html', context)



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

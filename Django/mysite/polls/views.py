from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import render, get_object_or_404     # index파일을 그려주기 위한 렌더
from django.http import Http404
from django.urls import reverse
from django.db.models import F  #DB를 바로 사용가능하도록 하는 메서드

def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    # output = ', '.join([q.question_text for q in latest_question_list])
    return render(request, 'polls/index.html', context)  # 템플릿을 사용하는 방법

def detail(request, question_id):
    """
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    """
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #detail.html에서 input이름을 choice로 받기 떄문에 POST에서 초이스로 선택
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_message':f"선택이 없습니다. id={request.POST.get('choice', 'None')}"})
    # except KeyError:
        # return render(request, 'polls/detail.html', {'question':question, 'error_message':f"선택이 없습니다"})
    else:
        # selected_choice.votes += 1  # 서버가 둘 이상일 때 서버에서 계산 하는 것이 문제될 수 있다.
        selected_choice.votes = F('votes') + 1 # 서버에서 바로 반영되도록 코드 수정
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))

def result(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/result.html', {'question':question})
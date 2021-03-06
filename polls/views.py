from django.shortcuts import render
from polls.models import Question, Choice

def index(request):
    #설문 메인
    question_list = Question.objects.all()
    context = {'question_list':question_list}
    return render(request, 'polls/poll_list.html', context)

def detail(request, pk):
    # 설문 상세
    #해당 id(순번)로 자료 조회(select)
    question = Question.objects.get(id=pk)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, pk):
    # 투표 하기
    question = Question.objects.get(id=pk)
    #선택 자료 넘겨 받음
    try:
        choice_id = request.POST['choice']
        sel_choice = question.choice_set.get(id=choice_id)
    except:
        context = {'question':question, 'error':'선택을 확인하세요'}
        return render(request, 'polls/detail.html', context)
    else:
        sel_choice.votes = sel_choice.votes + 1
        sel_choice.save()   #db에 저장
        return render(request, 'polls/vote.html', {'question':question})
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import AnswerForm
from ..models import Question, Answer



@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    # print("답변 등록 페이지 실행")
    # # form 엘리멘트에 입력된 값을 받아 데이터베이스에 저장할 수 있게함
    # question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # # redirect 함수는 함수에 전달된 값을 참고하여 페이지 이동을 수행한다.
    # return redirect('pybo:detail', question_id=question.id)



    print("테스트11")
    question = get_object_or_404(Question, pk=question_id)
    print(request.method)
    if(request.method == "POST"):
        print("테스트1")
        form = AnswerForm(request.POST)
        print("테스트2")
        if form.is_valid():
            print("테스트4")
            answer = form.save(commit=False)
            print("테스트5")
            answer.author = request.user    # 추가한 속성 author 적용
            print("테스트6")
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            #return redirect('pybo:detail', question_id = question_id)
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=question.id), answer.id))
    else:
        print("테스트111")
        form = AnswerForm()
        print("테스트112")
        context = {'question': question, 'form':form}
        print("테스트113")
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    pybo 답변수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            #return redirect('pybo:detail', question_id=answer.question.id)
            return redirect('{}#answer_{}'.format(
            resolve_url('pybo:detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    pybo 답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)

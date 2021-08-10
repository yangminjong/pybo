from django.shortcuts import render
from .models import Question, Answer, Comment
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import QuestionForm, AnswerForm, CommentForm
#
# def index(request):
#     """
#     pybo 목록 출력
#     """
#     # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
#
#     # 입력 인자
#     page = request.GET.get('page', '1') # 페이지
#
#     # order_by 함수는 조회한 데이터를 특정 속성으로 정렬 -create_date는 작성일시의 역순
#     question_list = Question.objects.order_by('-create_date')
#     #context = {'question_list': question_list}
#
#     # 페이징 처리
#     paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
#     page_obj = paginator.get_page(page)
#
#     context = {'question_list': page_obj}
#     # render 함수는 context에 있는 Question 모델 데이터 question_list를  pybo/question_list.html 파일에 적용하여 HTML코드로 변환
#     return render(request, 'pybo/question_list.html', context)
#
# def detail(request, question_id):
#     """
#     pybo 내용 출력
#     """
#     #question = Question.objects.get(id=question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'pybo/question_detail.html', context)

# @login_required(login_url='common:login')
# def answer_create(request, question_id):
#     """
#     pybo 답변 등록
#     """
#     # print("답변 등록 페이지 실행")
#     # # form 엘리멘트에 입력된 값을 받아 데이터베이스에 저장할 수 있게함
#     # question = get_object_or_404(Question, pk=question_id)
#     # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
#     # # redirect 함수는 함수에 전달된 값을 참고하여 페이지 이동을 수행한다.
#     # return redirect('pybo:detail', question_id=question.id)
#
#     print("테스트11")
#     question = get_object_or_404(Question, pk=question_id)
#     print(request.method)
#     if(request.method == "POST"):
#         print("테스트1")
#         form = AnswerForm(request.POST)
#         print("테스트2")
#         if form.is_valid():
#             print("테스트4")
#             answer = form.save(commit=False)
#             print("테스트5")
#             answer.author = request.user    # 추가한 속성 author 적용
#             print("테스트6")
#             answer.create_date = timezone.now()
#             answer.question = question
#             answer.save()
#             return redirect('pybo:detail', question_id = question_id)
#     else:
#         print("테스트111")
#         form = AnswerForm()
#         print("테스트112")
#         context = {'question': question, 'form':form}
#         print("테스트113")
#     return render(request, 'pybo/question_detail.html', context)


# @login_required(login_url='common:login')
# def question_create(request):
#     """
#     pybo 질문 등록
#     """
#     if request.method == 'POST':
#         print('질문 등록 POST')
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.author = request.user
#             question.create_date = timezone.now()
#             question.save()
#             return redirect('pybo:index')
#     else:
#         form = QuestionForm() # request.method가 'GET'인 경우 호출
#         print('질문 등록 GET')
#         context = {'form': form}
#     return render(request, 'pybo/question_form.html', context)
#
#
# # 질문 수정 함수 추가하기
# @login_required(login_url='common:login')
# def question_modify(request, question_id):
#     """
#     pybo 질문수정
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '수정권한이 없습니다.')
#         return redirect('pybo:detail', question_id=question_id)
#     if request.method == "POST":
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.author = request.user
#             question.modify_date = timezone.now()
#             question.save()
#             return redirect('pybo:detail', question_id=question_id)
#     else:
#         form = QuestionForm(instance=question)
#     context = {'form': form}
#     return render(request, 'pybo/question_form.html', context)

# 질문 삭제 함수 추가
# @login_required(login_url='common:login')
# def question_delete(request, question_id):
#     """
#     pybo 질문 삭제
#     """
#     print('테스트!!!!')
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '삭제권한이 없습니다.')
#         return redirect('pybo:detail', question_id=question_id)
#     question.delete()
#     return redirect('pybo:index')
# @login_required(login_url='common:login')
# def question_delete(request, question_id):
#     """
#     pybo 질문삭제
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '삭제권한이 없습니다')
#         return redirect('pybo:detail', question_id=question.id)
#     question.delete()
#     return redirect('pybo:index')

# @login_required(login_url='common:login')
# def answer_modify(request, answer_id):
#     """
#     pybo 답변수정
#     """
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=answer.question.id)
#
#     if request.method == "POST":
#         form = AnswerForm(request.POST, instance=answer)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.modify_date = timezone.now()
#             answer.save()
#             return redirect('pybo:detail', question_id=answer.question.id)
#     else:
#         form = AnswerForm(instance=answer)
#     context = {'answer': answer, 'form': form}
#     return render(request, 'pybo/answer_form.html', context)
#
#
# @login_required(login_url='common:login')
# def answer_delete(request, answer_id):
#     """
#     pybo 답변삭제
#     """
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '삭제권한이 없습니다')
#     else:
#         answer.delete()
#     return redirect('pybo:detail', question_id=answer.question.id)


#
# @login_required(login_url='common:login')
# def comment_create_question(request, question_id):
#     """
#     pybo 질문댓글등록
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.create_date = timezone.now()
#             comment.question = question
#             comment.save()
#             return redirect('pybo:detail', question_id=question.id)
#     else:
#         form = CommentForm()
#     context = {'form': form}
#     return render(request, 'pybo/comment_form.html', context)
#
#
# @login_required(login_url='common:login')
# def comment_modify_question(request, comment_id):
#     """
#     pybo 질문댓글수정
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=comment.question.id)
#
#     if request.method == "POST":
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.modify_date = timezone.now()
#             comment.save()
#             return redirect('pybo:detail', question_id=comment.question.id)
#     else:
#         form = CommentForm(instance=comment)
#     context = {'form': form}
#     return render(request, 'pybo/comment_form.html', context)
#
#
#
#
#
# @login_required(login_url='common:login')
# def comment_delete_question(request, comment_id):
#     """
#     pybo 질문댓글삭제
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글삭제권한이 없습니다')
#         return redirect('pybo:detail', question_id=comment.question.id)
#     else:
#         comment.delete()
#     return redirect('pybo:detail', question_id=comment.question.id)
#
#
#
#
# @login_required(login_url='common:login')
# def comment_create_answer(request, answer_id):
#     """
#     pybo 답글댓글등록
#     """
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.create_date = timezone.now()
#             comment.answer = answer
#             comment.save()
#             return redirect('pybo:detail', question_id=comment.answer.question.id)
#     else:
#         form = CommentForm()
#     context = {'form': form}
#     return render(request, 'pybo/comment_form.html', context)
#
#
# @login_required(login_url='common:login')
# def comment_modify_answer(request, comment_id):
#     """
#     pybo 답글댓글수정
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=comment.answer.question.id)
#
#     if request.method == "POST":
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.modify_date = timezone.now()
#             comment.save()
#             return redirect('pybo:detail', question_id=comment.answer.question.id)
#     else:
#         form = CommentForm(instance=comment)
#     context = {'form': form}
#     return render(request, 'pybo/comment_form.html', context)
#
#
# @login_required(login_url='common:login')
# def comment_delete_answer(request, comment_id):
#     """
#     pybo 답글댓글삭제
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글삭제권한이 없습니다')
#         return redirect('pybo:detail', question_id=comment.answer.question.id)
#     else:
#         comment.delete()
#     return redirect('pybo:detail', question_id=comment.answer.question.id)
#










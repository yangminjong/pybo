from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
from django.db.models import Q, Count



def index(request):
    """
    pybo 목록 출력
    """
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

    # 입력 인자
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '')      # 검색어
    # so = request.GET.get('so', 'recent') # 정렬 기준
    so = request.GET.get('so', 'recent')  # 정렬기준
    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    # order_by 함수는 조회한 데이터를 특정 속성으로 정렬 -create_date는 작성일시의 역순
    # question_list = Question.objects.order_by('-create_date')
    #context = {'question_list': question_list}

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |                 # 제목 검색
            Q(content__icontains=kw) |                 # 내용 검색
            Q(author__username__icontains=kw) |        # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
        

    # 페이징 처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page' : page, 'kw': kw} # page와 kw가 추가됨
    # render 함수는 context에 있는 Question 모델 데이터 question_list를  pybo/question_list.html 파일에 적용하여 HTML코드로 변환
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
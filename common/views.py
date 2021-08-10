from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm

def signup(request):
    """
    회원가입
    """
    if request.method == "POST":
        # POST 요청일 경우 화면에서 입력한 새로운 사용자를 생성
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        # GET요청일 경우 common/signup.html 화면을 반환
        form = UserForm()
    return render(request, 'common/signup.html', {'form':form})

# Create your views here.


def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})
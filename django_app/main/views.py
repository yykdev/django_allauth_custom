from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, authenticate

from main.forms import LoginForm


# 1단계 : 로그인
# 실 서비스에서는 1단계는 이메일, 유저명 전화번호 입력 후 다음 버튼 클릭시 회원 가입 / 로그인 / 2단계 이동 함.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('main:social')
    context = {

    }
    return render(request, 'index.html', context=context)


# 2단계 : 로그인 후 소셜 인증 버튼 페이지 렌더링
def social(request):
    print('social : ', request.user)
    context = {

    }
    return render(request, 'social.html', context=context)


# 3단계 소셜 인증 후 렌더링 될 페이지 ( 현재 유저 정보 출력 밖에 없음 )
def main(request):
    print('main : ', request.user)
    if request.method == 'POST':
        print('POST')
    context = {

    }
    return render(request, 'main.html', context=context)

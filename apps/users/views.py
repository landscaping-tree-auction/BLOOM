from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserLoginForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def user_signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            # return redirect('index')  # 'home'은 홈페이지로의 라우트명입니다. 적절히 변경해주세요.
            return HttpResponse('회원가입 성공')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('로그인 성공')
            else:
                messages.info(request, '계정을 찾을 수 없습니다.')
                return redirect('users:login')
        else:
            messages.info(request, '이메일 또는 비밀번호를 다시 확인해주세요.')
            return redirect('users:login')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return HttpResponse('로그아웃 성공')

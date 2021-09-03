from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model #사용자가 있는지 검사하는 함수
from django.contrib import auth

# 해당 html을 띄워주는 함수
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)
        #post 요청에 담겨진 데이터를 받아옴
        if password != password2:
            return render(request, 'user/signup.html') #페이지를 다시 띄움
        else: #password가 제대로 입력 됐다면
            exist_user = get_user_model().objects.filter(username=username)
            # exist_user = UserModel.objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')  # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else: #데이터베이스에 저장
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                # new_user = UserModel()
                # new_user.username = username
                # new_user.password = password
                # new_user.bio = bio
                # new_user.save()
                return redirect('/sign-in') #회원가입 완료 시 로그인 페이지 실행

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # post 요청에 담겨진 데이터를 받아옴
        me = auth.authenticate(request, username=username, password=password) #암호화된 비밀번호와 실제 비밀번호가 맞는지 검사
        #me = UserModel.objects.get(username=username) #UserModel db에서 username값이 받아온 데이터와 같은지 확인
        #if me.password == password: #me의 password값이 같은지 확인
        if me is not None:
            auth.login(request, me)
            #request.session['user'] = me.username
            return redirect('/')
        else:
            return redirect('/sign-in')
    elif request.method == 'GET':
        return render(request, 'user/signin.html')
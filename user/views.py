from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse

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
        else:
            new_user = UserModel()
            new_user.username = username
            new_user.password = password
            new_user.bio = bio
            #new_user안에 데이터 저장
            new_user.save() #데이터베이스에 저장

        return redirect('/sign-in') #회원가입 완료 시 로그인 페이지 실행


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # post 요청에 담겨진 데이터를 받아옴
        me = UserModel.objects.get(username=username) #UserModel db에서 username값이 받아온 데이터와 같은지 확인
        if me.password == password: #me의 password값이 같은지 확인
            request.session['user'] = me.username
            return HttpResponse("로그인 성공!")
        else:
            return  redirect('/sign-in')
    elif request.method == 'GET':
        return render(request, 'user/signin.html')
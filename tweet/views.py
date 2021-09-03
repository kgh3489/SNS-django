from django.shortcuts import render, redirect

def home(request):
    user = request.user.is_authenticated #유저가 로그인(인증)이 되어있는지 확인
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

def tweet(request):
    if request.method == 'GET':
        return render(request, 'tweet/home.html')

from django.shortcuts import render, redirect
from .models import TweetModel

def home(request):
    user = request.user.is_authenticated #유저가 로그인(인증)이 되어있는지 확인
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'tweet/home.html')
        else:
            return redirect('/sign-in')

    elif request.method == 'POST':
        user = request.user #request.user:지금 로그인 되어있는 사용자의 정보를 불러움
        my_tweet = TweetModel()
        my_tweet.author = user
        my_tweet.content = request.POST.get('my-content','')
        my_tweet.save()
        return redirect('/tweet')
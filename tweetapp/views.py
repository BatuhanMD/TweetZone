from django.shortcuts import render,redirect
from . import models
from django.urls import reverse
# Create your views here.


def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dic = {"tweets":all_tweets}
    return render(request,"tweetapp/listtweet.html",context=tweet_dic)

def addtweet(request):
    if request.POST:
        nick = request.POST["nickname"]
        message = request.POST["message"]
        models.Tweet.objects.create(nickname=nick,message=message)
        return redirect(reverse("tweetapp:ListTweet"))
    return render(request,"tweetapp/addtweet.html")

from django.shortcuts import render,redirect
from . import models
from django.urls import reverse, reverse_lazy
from tweetapp.forms import AddTweetForm, AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dic = {"tweets":all_tweets}
    return render(request,"tweetapp/listtweet.html",context=tweet_dic)


@login_required(login_url="/login") #Tweet atmak için login kıstası koyduk
def addtweet(request):
    if request.POST:
        nick = request.POST["nickname"]
        message = request.POST["message"]
        models.Tweet.objects.create(nickname=nick,message=message)
        return redirect(reverse("tweetapp:ListTweet"))
    return render(request,"tweetapp/addtweet.html")

def addtweetbyform(request):
    if request.POST:
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname=nickname, message=message)
            return redirect(reverse("tweetapp:ListTweet"))
        else:
            print("Error!")
            return render(request,"tweetapp/addtweetbyform.html",context={"form":form})
    else:
        form = AddTweetForm()
        return render(request,"tweetapp/addtweetbyform.html",context={"form":form})
    

def addtweetmodelform(request):
    if request.POST:
        nick = request.POST["nickname"]
        message = request.POST["message"]
        models.Tweet.objects.create(nickname=nick,message=message)
        return redirect(reverse("tweetapp:ListTweet"))
    return render(request,"tweetapp/addtweet.html")

def addtweetbyform(request):
    if request.POST:
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname, message=message)
            return redirect(reverse("tweetapp:ListTweet"))
        else:
            print("Error!")
            return render(request,"tweetapp/addtweetmodelform.html",context={"form":form})
    else:
        form = AddTweetModelForm()
        return render(request,"tweetapp/addtweetmodelform.html",context={"form":form})
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') #bellek tüketimini azaltmak için lazy
    template_name = "registration/signup.html"
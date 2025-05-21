from django.urls import path
app_name ="tweetapp"
from . import views

urlpatterns = [
    path('listtweet/', views.listtweet,name="ListTweet"),
    path("addtweet/",views.addtweet,name="AddTweet"),
    path('addtweetbyform/', views.addtweetbyform,name="AddTweetByForm"),
    path('addtweetmodelform/', views.addtweetmodelform,name="AddTweetModelForm"),
    path("signup/",views.SignUpView.as_view(),name="SignUp"),
    path("deletetweet/<int:id>",views.deletetweet,name="DeleteTweet")
]
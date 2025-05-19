from django.urls import path
app_name ="tweetapp"
from . import views

urlpatterns = [
    path('listtweet/', views.listtweet,name="ListTweet"),
    path("addtweet/",views.addtweet,name="AddTweet")
]
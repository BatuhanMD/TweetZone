from django import forms    
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(max_length="20",label="nickname")
    message_input = forms.CharField(max_length="255",label="message")


class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["nickname","message"]
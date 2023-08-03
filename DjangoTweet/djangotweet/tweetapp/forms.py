from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(max_length=15, label="Username")
    message_input = forms.CharField(max_length=250, label="Message", widget=forms.Textarea(attrs={"class":"tweetmessage"}))

class AddTweetModelForm(ModelForm): #yukarıdaki classı silebiliriz...
    class Meta:
        model = Tweet
        fields =["username", "message"]




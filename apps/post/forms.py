from django import forms

from apps.user.models import User


class NewPost(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    caption = forms.CharField(label='caption', widget=forms.Textarea)
    user = User.objects.get(email='eli@yahoo.com')

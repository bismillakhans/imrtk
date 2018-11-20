from django import forms
from .models import Comment


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'id': 'text-input', 'rows': '4'
    }))

    author_comment = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'author-input',
    }))

class ReplyForm(forms.Form):
    fk_comment = forms.IntegerField()
    reply = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'id': 'text-input-reply', 'rows': '2'
    }))

    author_reply = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'author-input-reply',
    }))


        
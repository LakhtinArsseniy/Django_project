from django import forms

from blog.models import Comment


class PostForm(forms.Form):
    content = forms.CharField()

    def clean_content(self):
        pass
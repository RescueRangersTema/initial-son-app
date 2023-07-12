from django import forms
from core import models


class CreateLessonArticleForm(forms.ModelForm):
    class Meta:
        model = models.LessonArticle
        fields = ['title', 'body']

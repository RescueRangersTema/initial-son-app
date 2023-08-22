from django import forms
from core import models


class CreateExcerciseArticleForm(forms.ModelForm):
    class Meta:
        model = models.ExcerciseArticle
        fields = ['title', 'body']

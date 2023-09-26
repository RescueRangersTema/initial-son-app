from django import forms
from core import models


class CreateUpdateExcerciseArticleForm(forms.ModelForm):
    class Meta:
        model = models.ExcerciseArticle
        fields = ['title', 'body', 'tags', 'excercises']


class AddTagForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = ['title']


class CreateUpdateExcercise(forms.ModelForm):
    class Meta:
        model = models.Excercise
        fields = ['title', 'problem', 'solution', 'explanation_solution', 'is_sample']

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . import forms
from core.models import LessonArticle


def index(request):
    return render(request, 'lesson/index.html')


@login_required
def create_lesson_article(request):

    form = None

    if request.method == "POST":
        form = forms.CreateLessonArticleForm(data=request.POST)

        if form.is_valid():
            form.instance.author = request.user
            new_article = form.save()

            return HttpResponseRedirect(reverse(
                'lesson:article', kwargs={'pk': new_article.id}
                ))

        messages.error(request, f'{form.errors}')

    form = forms.CreateLessonArticleForm()

    return render(
        request,
        'lesson/create-lesson-article.html',
        {'form': form}
    )


def view_lesson_article(request, pk):

    article = LessonArticle.objects.filter(pk=pk)
    if article.exists():

        return render(
            request,
            'lesson/lesson.html',
            {'context': article.values()[0]}
        )

    return render(
        request,
        'lesson/lesson.html',
        {'context': 'No such article'}
    )

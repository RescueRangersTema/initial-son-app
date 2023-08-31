from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . import forms
from core.models import ExcerciseArticle


def index(request):
    return render(request, 'lesson/index.html')


@login_required
def create_excercise_article(request):

    form = None

    if request.method == "POST":
        form = forms.CreateExcerciseArticleForm(data=request.POST)

        if form.is_valid():
            form.instance.author = request.user
            new_article = form.save()

            return HttpResponseRedirect(reverse(
                'lesson:article', kwargs={'pk': new_article.id}
                ))

        messages.error(request, f'{form.errors}')

    form = forms.CreateExcerciseArticleForm()

    return render(
        request,
        'lesson/create-lesson-article.html',
        {'form': form}
    )


def view_excercise_article(request, pk):
    article = ExcerciseArticle.objects.filter(pk=pk)

    context = {'context': article.first()}
    context["sample_task_amount"] = 2

    if article.exists():
        return render(
            request,
            'lesson/lesson.html',
            context,
        )

    return render(
        request,
        'lesson/lesson.html',
        {'context': 'No such article'}
    )


def view_sample_excercise_article(request):
    context = {'context': None}

    return render(
        request,
        'lesson/lesson.html',
        context
    )


def list_excercise_article(request):
    articles = ExcerciseArticle.objects.all()

    return render(
        request,
        'lesson/list_all.html',
        {'context': articles}
    )

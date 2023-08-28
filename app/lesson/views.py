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

    if article.exists():
        return render(
            request,
            'lesson/lesson.html',
            {'context': article.first()}
        )

    return render(
        request,
        'lesson/lesson.html',
        {'context': 'No such article'}
    )


def view_sample_excercise_article(request):
    # article = ExcerciseArticle.objects.filter(pk=pk)
    # if article.exists():

    #     return render(
    #         request,
    #         'lesson/lesson.html',
    #         {'context': article.values()[0]}
    #     )
    from .text_article import text
    article_text = text
    article_info = "I am a dog, I have paw"
    tasks_examples = [{"task_name": "elf",
                       "task_description":"Returns an HttpResponseRedirect to the appropriate URL for the arguments passed.",
                       "solution": {"Pseudocode": "gone", "python": "go", "C#": "went", "JS": "Something here", "Java": "here", "C++": "else"},
                       "info": "go",
                       "tags": ["animal", "hard"]},
                      {"task_name": "gnum",
                       "task_description": "The full name of a template to use or sequence of template names. If a sequence is given, the first template that exists will be used. See the template loading documentation for more information on how templates are found.",
                       "solution": {"Pseudocode": "gone", "python": "go", "C#": "went", "JS": "Something here", "Java": "here", "C++": "else"},
                       "info": "hi",
                       "tags": ["hard"]},
                      {"task_name": "human",
                       "task_description": "A dictionary of values to add to the template context. By default, this is an empty dictionary. If a value in the dictionary is callable, the view will call it just before rendering the template.",
                       "solution": {"Pseudocode": "gone", "python": "go", "C#": "went", "JS": "Something here", "Java": "here", "C++": "else"},
                       "info": "alive",
                       "tags": ["hard", "easy"]},
                      ]
    tasks_problems = [{}]
    article_similar = [{}]

    context = {'context': {
            "article_text": article_text,
            "article_info": article_info,
            "tasks_examples": tasks_examples,
            "tasks_problems": tasks_problems,
            "article_similar": article_similar,
        }
    }

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

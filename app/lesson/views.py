from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . import forms
from core import models


def index(request):
    return render(request, 'lesson/index.html')


@login_required
def create_excercise_article(request):

    form = None

    if request.method == "POST":
        form = forms.CreateUpdateExcerciseArticleForm(data=request.POST)

        if form.is_valid():
            form.instance.author = request.user
            new_article = form.save()

            return HttpResponseRedirect(reverse(
                'article:article', kwargs={'pk': new_article.id}
                ))

        messages.error(request, f'{form.errors}')

    form = forms.CreateUpdateExcerciseArticleForm()

    return render(
        request,
        'lesson/create-update-lesson-article.html',
        {'form': form}
    )


@login_required
def update_excercise_article(request, pk):
    article = models.ExcerciseArticle.objects.filter(pk=pk)
    if not article.exists():
        return render(
            request,
            'lesson/lesson.html',
            {'context': 'No such article'}
        )
    form = forms.CreateUpdateExcerciseArticleForm(instance=article.first())

    if request.method == "POST":
        form = forms.CreateUpdateExcerciseArticleForm(data=request.POST)

        if form.is_valid():
            form.instance.author = request.user
            new_article = form.save()

            return HttpResponseRedirect(reverse(
                'article:article', kwargs={'pk': new_article.id}
                ))

        messages.error(request, f'{form.errors}')

    return render(
        request,
        'lesson/create-update-lesson-article.html',
        {
            'form': form, 
            'id': article.first().id
        }
    )


@login_required
def add_tag(request):

    form = None

    if request.method == "POST":
        form = forms.AddTagForm(data=request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()

            return HttpResponseRedirect(reverse(
                'article:list_excercise_articles', kwargs={'page': 1}
                ))

        messages.error(request, f'{form.errors}')

    
    form = forms.AddTagForm()
    
    return render(
        request,
        'lesson/create-update-tag.html',
        {'form': form,}
    )


def list_excercise(request, page):
    excercises = models.Excercise.objects.all().order_by('-id')

    paginator = Paginator(excercises, per_page=2)
    page_object = paginator.get_page(page)

    context = {"page_obj": page_object}

    return render(
        request,
        'lesson/list_excercises.html',
        context
    )


@login_required
def add_excercise(request):

    form = None

    if request.method == "POST":
        form = forms.CreateUpdateExcercise(data=request.POST)

        if form.is_valid():
            form.instance.author = request.user
            form.save()

            return HttpResponseRedirect(reverse(
                'article:list_excercise_articles', kwargs={'page': 1}
                ))

        messages.error(request, f'{form.errors}')

    form = forms.CreateUpdateExcercise()

    return render(
        request,
        'lesson/create-update-excercise.html',
        {'form': form,}
    )


@login_required
def update_excercise(request, pk):
    excercise = models.Excercise.objects.filter(pk=pk)
    if not excercise.exists():
        return render(
            request,
            'lesson/lesson.html',
            {'context': 'No such article'}
        )
    form = forms.CreateUpdateExcercise(instance=excercise.first())

    if request.method == "POST":
        form = forms.CreateUpdateExcercise(data=request.POST)

        if form.is_valid():
            form.instance.author = request.user
            new_excercise = form.save()

            return HttpResponseRedirect(reverse(
                'article:list_excercise', kwargs={'page': 1}
                ))

        messages.error(request, f'{form.errors}')

    return render(
        request,
        'lesson/create-update-excercise.html',
        {
            'form': form, 
            'id': excercise.first().id
        }
    )


def view_excercise_article(request, pk):
    article = models.ExcerciseArticle.objects.filter(pk=pk)

    if article.exists():

        sample_excercises = article.first().excercises.filter(is_sample=True)
        excercises = article.first().excercises.filter(is_sample=False)
    
        context = {
            'context': article.first(),
            'sample_excercises': sample_excercises,
            'excercises': excercises,
            }

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


def list_excercise_article(request, page):
    articles = models.ExcerciseArticle.objects.all().order_by('-id')

    paginator = Paginator(articles, per_page=2)
    page_object = paginator.get_page(page)

    context = {"page_obj": page_object}

    return render(
        request,
        'lesson/list_all.html',
        context
    )

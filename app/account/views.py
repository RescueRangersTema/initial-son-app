from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from . import forms


def index(request):
    return render(request, 'account/index.html')


def sign_in(request):

    if request.user.is_authenticated:
        return redirect('account:index')

    if request.method == 'POST':
        form = forms.UserLoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('account:index'))
            else:
                messages.error(request, 'Invalid username of password')
        messages.error(request, f'{form.errors}')

    form = forms.UserLoginForm()

    return render(request, 'account/login.html', {'form': form})


@login_required
def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('account:index')

    return render(request, 'account/logout.html')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('account:index')

    if request.method == 'POST':
        form = forms.UserCreationForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('account:index')

        messages.error(request, f'{form.errors}')

    user_creation_form = forms.UserCreationForm()
    return render(
        request, 'account/sign-up.html', {'form': user_creation_form}
    )

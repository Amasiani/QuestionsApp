from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm, AccountUpdateForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        #request.session.set_expiry(0)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)



def logout_view(request):
    logout(request)
    return redirect('/')



def account_view(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial = {
                'email' : request.user.email,
                'username': request.user.username
            }
        )

    context = {
        'form': form
    }
    return render(request, 'account.html', context)
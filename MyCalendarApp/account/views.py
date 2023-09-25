from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from account.forms import AccountAuthenticationForm, RegistrationForm


# Create your views here

def loginView(request):
    context = {}
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=email,password=password)
            login(request,user)
            return redirect('home')
    else:
        form = AccountAuthenticationForm()
    context['form'] = form
    return render(request, "login.html", context)


def logoutView(request):
    logout(request)
    return redirect("login")


def registerView(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    context['form'] = form
    return render(request, "register.html", context)

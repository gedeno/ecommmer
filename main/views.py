from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,logout, authenticate
from django.contrib.auth.forms import UserCreationFrom
from django.contrib.auth.models import User

# Create your views here.
def registration(requeset):
    form = UserCreationFrom()
    if requeset.method == "post":
        form = UserCreationFrom(requeset.POST)
        if form.is_valid():
            form.save()
            return redirect('login')


from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def registration(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'main/register.html',{'form':form})
def logins(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=Username,password=password)
        if user != None:
            login(request.user)
            return redirect('home')
    return render(request,'main/login.html')
@login_required(login_url='login/')
def home(request):
    return render(request,'main/home.html')



from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Normal_product,Phone_product,Laptop_product
from .forms import Normal_product_form,Phone_product_form,Laptop_product_form

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
            login(request, user)
            if user.is_superuser:
                return redirect('superhome')
            return redirect('home')
    return render(request,'main/login.html')
@login_required(login_url='login/')
def home(request):
    return render(request,'main/home.html')
def superhome(request):
    form = Normal_product_form()
    if request.method == 'POST':
        form = Normal_product_form(request.POST, request.FILES)
        add_info  = request.POST.get('info')
        if add_info == 'phone':
            if form.is_valid():
                a = form.save()
                return redirect(f'/superphone/{a.id}')
    return render(request, 'main/superhome.html', {'form': form})

def superphone(request,id):
    product = Normal_product.objects.get(id = id)
    form = Phone_product_form()
    if request.method == 'POST':
        form = Phone_product_form(request.POST)
        if form.is_valid():
            phone = form.save(commit=False)
            phone.all_info = product
            phone.save()
            return redirect('superhome')
    return render(request, 'main/superphone.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')


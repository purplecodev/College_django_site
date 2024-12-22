from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from .forms import  UserRegisterForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались и приняли участие в розыгрыше!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/register.html', {'form': form})

def userlogin(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли!')
            return redirect('home')
    else:
        form = UserLoginForm()


    return render(request, 'authentication/login.html', {'form': form})



def userlogout(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли!')
    return redirect('login')
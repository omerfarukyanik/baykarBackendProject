from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .utils import serialize_messages


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            messages.success(request, "Signup successful")
            return redirect('main_page')
        else:
            messages.error(request, "Authentication failed")
            return redirect('signup')

    context = serialize_messages(messages, request)
    return render(request, 'signup.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home_page')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    context = serialize_messages(messages, request)
    return render(request, 'login.html', context)


@login_required
def home_page(request):
    return render(request, 'home_page.html')

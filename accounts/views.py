from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth 


def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST ["password2"]:
            user = User.objects.create_user(
                username = request.POST['username'], password = request.POST['password']
            )
            return redirect('home')
    return render(request, 'signup.html')


# Create your views here.

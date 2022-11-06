from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout


@login_required(login_url='usuario:login')
def index(request):
    return render(request, "base/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "usuario/login.html", {"msj": "Credenciales incorrectas"})
    return render(request, "usuario/login.html")


def logout_view(request):
    logout(request)
    return render(request, "usuario/login.html", {"msj": "Deslogueado"})

from django.shortcuts import render


def singup(request):
    return render(request, "users/singup.html")


def singin(request):
    return render(request, "users/singin.html")

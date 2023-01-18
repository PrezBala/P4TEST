from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})


def home(request):
    return render(request, "detail.html", {})


def home(request):
    return render(request, "posts.html", {})

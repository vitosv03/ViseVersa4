from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This is about page')


def home(request):
    return render(request, 'home.html')


def reverse(request):
    return render(request, 'reverse.html')

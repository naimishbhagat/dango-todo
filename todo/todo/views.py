from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    template = 'index.html'
    return render(request, template, {})

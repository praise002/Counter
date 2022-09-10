from django.shortcuts import render, redirect
from . forms import CountForm
from . models import Count


def home(request):
    return render(request, 'counts/home.html')


def count(request):
    text = request.POST['text']
    words = text.split()
    amount_of_words = len(words)
    context = {'words': amount_of_words}
    return render(request, 'counts/count.html', context)

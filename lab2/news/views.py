from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import art
from .forms import artForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = art.objects.all()
    return render(request, 'news/news.html', {'news': news})


def kom(request):
    news = art.objects.all()
    return render(request, 'news/kom.html', {'news': news})


class NewsDetailView(DetailView):
    model = art
    template_name = 'news/NewsDetailView.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = art
    template_name = 'news/create.html'

    form_class = artForm


class NewsDeleteView(DeleteView):
    model = art
    success_url = '/news/'
    template_name = 'news/NewsDeleteView.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = artForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'news/create_done.html')
        else:
            error = 'Ошибка'

    form = artForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)

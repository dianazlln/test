from django.shortcuts import render

# Create your views here.


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Спасибо за внимание!']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def cont(request):
    return render(request, 'main/cont.html')

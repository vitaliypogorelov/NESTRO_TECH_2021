from django.shortcuts import render

def index(request):
    context = {}    #с помощью словаря будем передать модель и форму в шаблон HTML
    return render(request, 'index.html', context)
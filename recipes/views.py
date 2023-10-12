from django.shortcuts import render


def home(request):

    return render(request, 'recipes/home.html') #Adicionar pasta no templates Para servir de namespace e não comflitar com arquivos de nome igual
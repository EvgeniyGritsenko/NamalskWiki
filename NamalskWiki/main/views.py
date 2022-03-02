from os import link
from django.shortcuts import render
from articles.models import ArticleModel, CategoryModel
from .forms import ContactWithAuthorForm

def mainPage(request):
    "Главная страница сайта"

    context = {
        "category": CategoryModel.objects.all(),
        "articles": ArticleModel.objects.all(),
    }
    return render(request, 'main/main_page.html' , context=context)



def ContactWithAuthor(request):
    "Связь с автором"

    if request.method == "POST":
        form = ContactWithAuthorForm(request.POST)
        if form.is_valid():
            new_message = form.save()
        else:
            print("Не удалось отправить в бд!")

    context = {
        "form": ContactWithAuthorForm(),
    }


    return render(request, 'main/contact_with_author.html', context=context)

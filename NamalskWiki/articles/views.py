from django.shortcuts import render, redirect
from .models import ArticleModel, CommentModel, CategoryModel, ContactWithAuthorModel
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CommentForm

def articlesMain(request):
    """Главная страница статей"""
    context = {
        "category": CategoryModel.objects.all(),
    }
    return render(request, 'articles/articles_main.html', context=context)


def articlesThisCategory(request, category_id):
    """Статьи по выбранной категории"""
    category = CategoryModel.objects.get(id=category_id)

    context = {
        "ctg": category,
    }
    return render(request, 'articles/this_category.html', context=context)


def thisArticle(request, article_id, category_id):
    """Выбранная статья и комментарии к ней"""
    if request.method == "POST":
        form = CommentForm(request.POST) # объект с полученными данными
        if form.is_valid(): # валидация данных
            new_comment = form.save(commit=False)
            new_comment.article = ArticleModel.objects.get(id=article_id)
            new_comment.save()
        else:
            print("Что-то не так!")

    article = ArticleModel.objects.get(id=article_id)

    context = {
        "article": article,
        "photos": [article.photo1, article.photo2, article.photo3],
        "form": CommentForm(),
    }


    return render(request, 'articles/article.html', context=context)




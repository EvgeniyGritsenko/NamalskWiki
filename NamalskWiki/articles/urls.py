from django.urls import path
from .views import articlesMain, articlesThisCategory, thisArticle

urlpatterns = [
    path('', articlesMain , name='articles_main'),
    path('<int:category_id>/', articlesThisCategory, name="articles_this_category"),
    path('<int:category_id>/article/<int:article_id>/', thisArticle, name="this_article"),
]
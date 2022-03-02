from django.contrib import admin
from .models import ArticleModel, CategoryModel, CommentModel, ContactWithAuthorModel


admin.site.register(ArticleModel)
admin.site.register(CategoryModel)
admin.site.register(CommentModel)
admin.site.register(ContactWithAuthorModel)

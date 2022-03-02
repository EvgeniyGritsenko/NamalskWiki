from django.db import models

# class ArticleModel(models.Model):
#     title = models.CharField(max_length=100, verbose_name="Заголовок")
#     content = models.TextField(verbose_name="Контент")
#     published = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано")

#     class Meta:
#         verbose_name = "Статья"
#         verbose_name_plural = "Статьи"
#         ordering = ['title']

#     def __str__(self) -> str:
#         return f"AritcleModel({self.id}, {self.title})"


# class CommentModel(models.Model):
#     pass

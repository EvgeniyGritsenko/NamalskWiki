from email.policy import default
from django.db import models

class ArticleModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    # images
    content = models.TextField(verbose_name="Описание")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Опубликована")
    category = models.ForeignKey('CategoryModel', null=False, on_delete=models.PROTECT, default=-1, related_name='articles')
    photo1 = models.ImageField(upload_to="images", default="NotFound")
    photo2 = models.ImageField(upload_to="images", default="NotFound")
    photo3 = models.ImageField(upload_to="images", default="NotFound")

    class Meta:
        verbose_name = "Статься"
        verbose_name_plural = "Статьи"
        ordering = ['-published']


    def __str__(self):
        return f"ArticleModel - <{self.pk}, {self.title}>"


class CategoryModel(models.Model):
    name = models.CharField(max_length=150)


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


    def __str__(self):
        return f"CategoryModel - <{self.pk}, {self.name}>"


class CommentModel(models.Model):
    nick = models.CharField(max_length=50, verbose_name="Ник")
    comment = models.CharField(max_length=300, verbose_name="Комментарий")
    article = models.ForeignKey('ArticleModel', null=True, on_delete=models.CASCADE, verbose_name='Статья', default=-1, related_name="comments")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Опубликован", null=False)
    
    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"
        ordering = ['-published']


    def __str__(self):
        return f"CommentModel - <{self.pk}, {self.nick}>"

class ContactWithAuthorModel(models.Model):
    email = models.EmailField(max_length=100, verbose_name="Email для обратой связи")
    message = models.TextField(verbose_name="Сообщение автору")
    published = published = models.DateTimeField(auto_now_add=True, verbose_name="Пришло в...", null=False)

    
    class Meta:
        verbose_name = "Связь с автором"
        verbose_name_plural = "Связь с автором"

    def __str__(self):
        return f"ContactWithAuthorModel - <{self.pk}, {self.email}>"
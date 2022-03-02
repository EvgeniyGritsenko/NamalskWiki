from .models import CommentModel
from django.forms import ModelForm, TextInput


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['nick', 'comment']
        widgets = {
            "nick": TextInput(attrs={
                'class': 'form-nick',
                'placeholder': 'Введи свой ник',
            }),
            "comment": TextInput(attrs={
                'class': 'form-comment',
                'placeholder': 'Напиши свое мнение...',
            })
        }
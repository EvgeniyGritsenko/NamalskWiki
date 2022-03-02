from articles.models import ContactWithAuthorModel
from django.forms import ModelForm, TextInput, Textarea


class ContactWithAuthorForm(ModelForm):
    class Meta:
        model = ContactWithAuthorModel
        fields = ['email', 'message']
        widgets = {
            "email": TextInput(attrs={
                "class": "form_email",
                "placeholder": "email...",
            }),
            "message": Textarea(attrs={
                "class": "form_message",
                "placeholder": "message...",
            })
        }


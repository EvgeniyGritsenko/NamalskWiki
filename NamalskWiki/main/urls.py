from django.urls import path
from .views import mainPage, ContactWithAuthor

urlpatterns = [
    path('', mainPage, name='main_page'),
    path('contact_with_author/', ContactWithAuthor , name="cont_with_auth")
]
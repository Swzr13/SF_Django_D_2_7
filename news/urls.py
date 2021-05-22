from django.contrib import admin
from django.urls import path
from .views import AutorList, NewsList, NewsDeteil

urlpatterns = [
    path('',NewsList.as_view()),
    path('autors', AutorList.as_view()),
    path('news', NewsList.as_view()),
    path('news/<int:pk>', NewsDeteil.as_view())

]
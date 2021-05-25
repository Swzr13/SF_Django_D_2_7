from django.contrib import admin
from django.urls import path
from .views import AutorList, NewsList, NewsDeteil, SearchNews, Post_add, PostUpdate, PostDelete

urlpatterns = [
    path('',NewsList.as_view()),
    path('autors', AutorList.as_view()),
    path('news/', NewsList.as_view(), name='news'),
    path('news/<int:pk>', NewsDeteil.as_view(), name='post_deteil'),
    path('search', SearchNews.as_view(), name='search_news'),
    path('add', Post_add.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDelete.as_view(), name='post_delete'),

]
from django.shortcuts import render
from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем
from .models import Author, Post, Category, Comment

# Create your views here.
# def Index(request):
#     return render(request, 'default.html')

class AutorList(ListView):
    model = Author
    template_name = 'news/Autors.html'
    context_object_name = 'autors'

class NewsList(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-date_add')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['there_news'] = False
        return context

class NewsDeteil(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'
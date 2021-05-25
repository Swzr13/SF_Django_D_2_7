from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # импортируем класс, который говорит нам о том, что в этом представлении мы будем
from .models import Author, Post, Category, Comment
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm

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
    paginate_by = 3
    form_class = PostForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['there_news'] = False
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


class SearchNews(ListView):
    model = Post
    template_name = 'news/search.html'
    context_object_name = 'search'
    queryset = Post.objects.order_by('-date_add')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['there_news'] = False
        context['filter'] = PostFilter(self.request.GET, self.get_queryset())
        return context

class NewsDeteil(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'

class Post_add(CreateView):
    template_name = 'news/add.html'
    form_class = PostForm

class PostUpdate(UpdateView):
    template_name = 'news/add.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDelete(DeleteView):
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = 'news'
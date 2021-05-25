from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

    def update_rating(self):
        rating_post_autor = sum(p.rating * 3 for p in Post.objects.filter(autor=self.id))
        print('Post',rating_post_autor)
        rating_comment_autor = sum(c.rating for c in Comment.objects.filter(autor=self.user))
        print('Comment', rating_comment_autor)
        rating_post_comment = sum(c.rating for c in Comment.objects.filter(post__autor=self.id))
        print('Post_comment', rating_post_comment)
        self.rating = rating_post_autor + rating_comment_autor + rating_post_comment
        self.save()

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Category(models.Model):
    name = models.CharField(max_length=254, default='Empty', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Post(models.Model):

    news = 'NW'
    article = 'AR'

    TYPE_POST = [
        (news, 'News'),
        (article, 'Article')
    ]
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    type_post = models.CharField(max_length=2, choices=TYPE_POST, default=news)
    date_add = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=254, default='Empty')
    category = models.ManyToManyField(Category, through='PostCategory')
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'

    def print_comment(self):
        list_comment = Comment.objects.filter(post=self.id).order_by('data_add')
        number_comment = 1
        for comment in list_comment:
            print('Комментарий №', number_comment)
            print('Дата', comment.data_add.strftime("%H.%M.%S %d-%m-%Y"))
            print('Автор', comment.autor)
            print('Рейтинг', comment.rating)
            print('Текст:', comment.text)
            number_comment += 1
            print('*' * 20)

    def __str__(self):
        return self.preview()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='Empty')
    data_add = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
from django.db import models
import datetime
from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment

#1) Создать двух пользователей (с помощью метода User.objects.create_user).
user1 = User.objects.create_user(username='User1')
user2 = User.objects.create_user(username='User2')

#2) Создать два объекта модели Author, связанные с пользователями.
autor1 = Author.objects.create(user = user1)
autor2 = Author.objects.create(user = user2)

#3) Добавить 4 категории в модель Category.
category1 = Category.objects.create(name = 'Category1')
category2 = Category.objects.create(name = 'Category2')
category3 = Category.objects.create(name = 'Category3')
category4 = Category.objects.create(name = 'Category4')

#4) Добавить 2 статьи и 1 новость.
post1 = Post.objects.create(autor = autor1, type_post = Post.article, title = 'Первая статья ', text = 'Тут будет текст нашей первой статьи')
post2 = Post.objects.create(autor = autor1, type_post = Post.article, title = 'Вторая статья ', text = 'Тут будет текст нашей второй статьи')
post3 = Post.objects.create(autor = autor2, type_post = Post.news, title = 'Первая новость ', text = 'Текст новости')

#5) Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
post1.category.add(category1)
post1.category.add(category2)
post2.category.add(category1)
post3.category.add(category4)

#6) Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
comment1 = Comment.objects.create(post = post1, autor = user1, text = 'Комментарий1 к первой статье')
comment2 = Comment.objects.create(post = post1, autor = user2, text = 'Комментарий2 к первой статье')
comment3 = Comment.objects.create(post = post2, autor = user2, text = 'Комментарий1 ко второй статье')
comment4 = Comment.objects.create(post = post3, autor = user2, text = 'Комментарий1 к новости')

#7) Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
post1.like()
post1.like()
post1.like()
post1.like()
post1.like()
post1.like()
post1.like()
post1.dislike()
post1.dislike()
# post1.rating = 5
post2.like()
post2.like()
post2.dislike()
post2.dislike()
post2.dislike()
post2.dislike()
# post2.rating = -2
post3.like()
post3.like()
post3.like()
post3.like()
# post3.rating = 4

comment1.like()
comment1.like()
comment1.like()
# comment1.rating = 3
comment2.like()
comment2.like()
# comment2.rating = 2
comment3.like()
comment3.like()
comment3.like()
comment3.dislike()
comment3.dislike()
# comment3.rating = 1
comment4.like()
# comment4.rating = 1

#8) Обновить рейтинги пользователей.
autor1.update_rating()
autor2.update_rating()

#9) Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
best_autor = Author.objects.filter().order_by('-rating').values('user__username','rating')[0]
print('Лучший автор -', best_autor.get('user__username'), 'с рейтингом', best_autor.get('rating'))

#10) Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
best_post_q = Post.objects.filter().order_by('-rating').values('id','date_add','autor__user__username','rating','title')[0]
id_best_post = best_post_q.get('id')
best_post = Post.objects.get(id = id_best_post) 
preview_best_post = best_post.preview()
print('Лучший пост:','"' + best_post_q.get('title') + '"','автора',best_post_q.get('autor__user__username'),'с рейтингом',best_post_q.get('rating'))
print('Дата добавления -', best_post_q.get('date_add').strftime("%H.%M.%S %d-%m-%Y"))
print('Превью -', preview_best_post)

#11) Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
best_post.print_comment()

from django.db import models
from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment
user1 = User.objects.get(username='User1')
user2 = User.objects.get(username='User2')
autor1 = Author.objects.get(user = user1)
autor2 = Author.objects.get(user = user2)
category1 = Category.objects.get(name = 'Category1')
category2 = Category.objects.get(name = 'Category2')
category3 = Category.objects.get(name = 'Category3')
category4 = Category.objects.get(name = 'Category4')
post1 = Post.objects.get(id = 1)
post2 = Post.objects.get(id = 2)
post3 = Post.objects.get(id = 3)
comment1 = Comment.objects.get(id = 1)
comment2 = Comment.objects.get(id = 2)
comment3 = Comment.objects.get(id = 3)
comment4 = Comment.objects.get(id = 4)


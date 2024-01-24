from django.contrib.auth.models import User
from django.db.models import Sum
from django.db import models
# from django.urls import reverse
from django.core.cache import cache

# Модель, содержащая объекты всех авторов
class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)

    def update_rating(self):
        posts_rating = Post.objects.filter(author=self).aggregate(result=Sum('rating')).get('result')
        comments_rating = Comment.objects.filter(user=self.user).aggregate(result=Sum('rating')).get('result')
        comment_post = Comment.objects.filter(post__author__user=self.user).aggregate(result=Sum('rating')).get('result')

        self.rating = (posts_rating * 3 + comments_rating + comment_post)
        self.save()

    def __str__(self):
        return self.user.username


# Модель, содержащая категории новостей/статей
class Category(models.Model):
    category = models.CharField(max_length = 255, unique = True)
    subscribers = models.ManyToManyField(User, related_name='categories', blank=True)

    def subscribe(self):
        ...

    def get_category(self):
        return self.name


    def __str__(self):
        return self.category.title()

# Данная модель содержит статьи и новости
class Post(models.Model):

    article = "AR"
    news = "NW"

    TYPE = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    post_type = models.CharField(max_length = 2, choices=TYPE, default=article)
    time_in = models.DateTimeField(auto_now_add = True)
    categories = models.ManyToManyField(Category, through = "PostCategory")
    title = models.CharField(max_length = 120)
    text = models.TextField(unique = True)
    rating = models.IntegerField(default = 0)

    def preview(self):
        return self.text[:124] + '...' if len(self.text) > 124 else self.text

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.title.title()

    # def get_absolute_url(self):
    #     return reverse('news_detail', args=[str(self.id)])

    def get_absolute_url(self):
        return f'/all-posts/{self.id}'


# Промежуточная модель для связи «многие ко многим» для связи с моделями Post и Category
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

# Модель хранящая комментарии для новостей и статей
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
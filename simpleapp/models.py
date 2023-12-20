from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

class Author(models.Model):
    user_rate = models.IntegerField(default=0)
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        sum_rating = self.post_set.aggregate(post_rating=Sum('post_rate'))
        result_sum_rating = 0
        try:
            result_sum_rating += sum_rating.get('post_rating')
        except TypeError:
            result_sum_rating = 0

        sum_comment_rating = self.author.comment_set.aggregate(comment_rating=Sum('comment_rate'))
        result_sum_comment_rating = 0
        result_sum_comment_rating += sum_comment_rating.get('comment_rating')

        self.user_rate = result_sum_rating * 3 + result_sum_comment_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscribers = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    name = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    article = 'A'
    news = 'N'

    POSITIONS = [
        (article, "Статься"),
        (news, "Новость"),
    ]

    category = models.CharField(max_length=1,
                                choices=POSITIONS,
                                default=news)
    dataCreations = models.DateField(auto_now_add=True)
    post_rate = models.IntegerField(default=0)

    def like(self):
        self.post_rate += 1
        self.save()

    def dislike(self):
        self.post_rate -= 1
        self.save()

    def preview(self):
        return self.content[:125]

    def __str__(self):
        return f'{self.title.title()}: {self.content[:20]}'



class PostCategory(models.Model):
    post_category = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category_category} | {self. post_category}'

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    comment_date_created = models.DateField(auto_now_add=True)
    comment_rate = models.IntegerField(default=0)

    def like(self):
        self.comment_rate += 1
        self.save()

    def dislike(self):
        self.comment_rate -= 1
        self.save()



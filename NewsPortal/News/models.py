from django.db import models
from django.contrib.auth.models import User

article = 'AR'
news = 'NE'

POST_TYPE = [
    (article, 'Статья'),
    (news, 'Новость')
]


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.IntegerField(default=0)


class Category(models.Model):
    name_category = models.CharField(max_length=40, unique=True)
    subscribers = models.ManyToManyField(User, related_name="categories")

    def __str__(self):
        return self.name_category


class Post(models.Model):
    post = models.ForeignKey(Author, on_delete=models.CASCADE)
    type_post = models.CharField(max_length=2, choices=POST_TYPE)
    date_post = models.DateTimeField(auto_now_add=True)
    category_post = models.ManyToManyField(Category, through='PostCategory')
    header_post = models.CharField(max_length=40)
    text_post = models.TextField()
    rating_post = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.header_post} : {self.text_post[:20]}'

    def preview(self):
        return f"{self.text_post[0:124]}..."

    @property
    def rating(self):
        return self.rating_post

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()
        
    def get_absolute_url(self):
        return f"/news/{self.id}"


class PostCategory(models.Model):
    post_category = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    @property
    def rating(self):
        return self.rating_comment

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()

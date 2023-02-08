from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        self.rating = 0
        posts = Post.objects.filter(author=self)
        for post in posts:
            self.rating += post.rating * 3
            comments = Comment.objects.filter(post=post)
            for comment in comments:
                self.rating += comment.rating
            own_comments = Comment.objects.filter(user=self.user)
            for own_comment in own_comments:
                self.rating += own_comment.rating

        self.save()

    # def __str__(self):
    #     return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    NEWS = 'NWS'
    ARTICLE = 'ART'
    CATEGORY_CHOISE = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )

    category_type = models.CharField(max_length=3, choices=CATEGORY_CHOISE, default=ARTICLE)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ManyToManyField(Category, through='PostCategory')
    create_at = models.DateTimeField(auto_now_add=True)
    updare_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + ' ... '

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.text

class PostCategory(models.Model):
    post_through = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_through = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title + ' ' + self.category.name

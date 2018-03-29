from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    user_name = models.CharField('user_name', max_length=45, blank=False)
    user_password = models.CharField('user_password', max_length=45, blank=False)
    user_email = models.EmailField('user_email', blank=False)


    def __str__(self):
        return self.user_name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField('post_title', max_length=45, default='', blank=False)
    post_text = models.CharField('post_text', max_length=500, blank=False)
    post_date = models.DateTimeField('post_date', default=timezone.now, blank=False)

    def __str__(self):
        return self.post_title

    def new_posts(self):
        


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_date = models.DateField('comment_date', default=timezone.now, blank=False)
    comment_text = models.CharField('comment_text', max_length=150, blank=False)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vode_date = models.DateTimeField('vote_date', default=timezone.now, blank=False)



    
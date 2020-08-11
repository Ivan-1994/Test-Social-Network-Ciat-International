from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='post',
                             on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='user_like_post')
    unlike = models.ManyToManyField(User, related_name='user_unlike_post')


# class PostLike(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              related_name='user_likes',
#                              on_delete=models.CASCADE)
#     post = models.ForeignKey(Post,
#                               related_name='post_likes',
#                               on_delete=models.CASCADE)


# class PostUnLike(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              related_name='user_unlikes',
#                              on_delete=models.CASCADE)
#     post = models.ForeignKey(Post,
#                               related_name='post_unlikes',
#                               on_delete=models.CASCADE)

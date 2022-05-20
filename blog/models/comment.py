from django.contrib.auth.models import User
from django.db import models

from blog.models import ArticleModel


class CommentModel(models.Model):
    comment = models.TextField()
    commenter = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, related_name='comments')
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
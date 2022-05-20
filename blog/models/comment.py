from django.contrib.auth.models import User
from django.db import models

from blog.abstract_models import DateAbstractModel
from blog.models import ArticleModel


class CommentModel(DateAbstractModel):
    comment = models.TextField()
    commenter = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, related_name='comments')


    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
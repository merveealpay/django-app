from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField

from blog.abstract_models import DateAbstractModel
from blog.models.category import CategoryModel


class ArticleModel(DateAbstractModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='article_images')
    body = RichTextField()

    slug = AutoSlugField(populate_from='title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='article')
    writer = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='articles')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        db_table = 'article'

    def __str__(self):
        return self.title
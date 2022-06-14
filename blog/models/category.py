from django.db import models
from autoslug import AutoSlugField


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=250, null=False, blank=False)
    slug = AutoSlugField(populate_from='category_name', unique=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

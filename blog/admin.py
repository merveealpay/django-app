from django.contrib import admin

from blog.models import CategoryModel, ArticleModel

admin.site.register(CategoryModel)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body')
    list_display = (
        'title', 'created_at', 'edited_at'
    )

admin.site.register(ArticleModel, ArticleAdmin)

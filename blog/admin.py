from django.contrib import admin

from blog.models import CategoryModel, ArticleModel, CommentModel, ContactModel

admin.site.register(CategoryModel)


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body')
    list_display = (
        'title', 'created_at', 'updated_at'
    )


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('commenter__username',)
    list_display = ('commenter', 'comment', 'created_at', 'updated_at')


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('email',)
    list_display = ('email', 'created_at')


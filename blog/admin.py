from django.contrib import admin

from blog.models import CategoryModel, ArticleModel, CommentModel, ContactModel

admin.site.register(CategoryModel)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body')
    list_display = (
        'title', 'created_at', 'updated_at'
    )


admin.site.register(ArticleModel, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    search_fields = ('commenter__username',)
    list_display = ('commenter', 'comment', 'created_at', 'updated_at')


admin.site.register(CommentModel, CommentAdmin)


class ContactAdmin(admin.ModelAdmin):
    search_fields = ('email',)
    list_display = ('email', 'created_at')


admin.site.register(ContactModel, ContactAdmin)

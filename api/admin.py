from django.contrib import admin

from .models import Review, Comment


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title_id', 'author', 'pk')
    search_fields = ('title_id',)
    list_filter = ('title_id',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'text', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date',)


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)

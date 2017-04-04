from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

# Register your models here.
admin.site.register(Post)

admin.site.unregister(Post)

# 등록법 2
class PostAdmin(admin.ModelAdmin):
    #ModelAdmin 의 option : list_display
    list_display = ['id', 'title', 'content_size', 'created_at', 'updated_at']

    #list_display 의 customizing
    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content))

    content_size.short_description = '글자수'
admin.site.register(Post, PostAdmin)
admin.site.unregister(Post, PostAdmin)

# 등록법 3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #ModelAdmin 의 option : list_display
    list_display = ['id', 'title', 'content_size', 'created_at', 'updated_at']

    #list_display 의 customizing
    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content))

    content_size.short_description = '글자수'

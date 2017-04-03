from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)

admin.site.unregister(Post)

# 등록법 2
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']

admin.site.register(Post, PostAdmin)

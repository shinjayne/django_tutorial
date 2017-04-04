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
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

admin.site.register(Post, PostAdmin)
admin.site.unregister(Post)

# 등록법 3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #ModelAdmin 의 option : list_display
    list_display = ['id', 'title', 'content_size','status', 'created_at', 'updated_at']
    #ModelAdmin 의 option : Actions
    actions = ['make_published']
    #list_display 의 customizing
    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

    #Actions의 커스터마이징
    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') #QuerySet.update --뒷부분에서 자세히 다룸
        self.message_user(request, '{}건의 포스팅을 Publisehd 상태로 변경'.format(updated_count))
        #django message framework -- 뒷부분에서 자세히 다룰 예정
    make_published.short_description = '선택된 항목의 status를 published로 변경합니다.'

from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from polls.models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.unregister(Question)


# list_display 커스터마이징
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text','text_len', 'pub_date'] #속성으로 내장 메서드도 이용 가능 'text_len'

    def text_len(self, question): #질문길이를 지정하는 내장 메서드. question은 Question의 하나의 인스턴스를 지칭하는 듯
        #django는 파이썬 코드나 변수를 통해 보여지는 html태그에 대해 autoescape 를 진행 : 태그가 다른 문자로 표시됨
        #mark_safe 함수는 태그가 표현되도록 도와줌.
        return mark_safe('<strong>{}</strong>글자'.format(len(question.question_text)))



    text_len.short_description = '글자수' #admin.ModelAdmin 클래스에서 상속받은 속성인듯. 내장 메서드가 admin 페이지에서 어떻게 보일지 설정.


admin.site.register(Choice)

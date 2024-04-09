from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):  #admin 계정에서 보기 이쁘게 만들어주는 함수
    fieldsets = [
        ('질문 섹션', {'fields': ['question_text']}),
        ('생성일', {'fields': ['pub_date'], 'classes': ['collapse']}),  #숨기고 싶을 때 classes에 collapse를 준다
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    readonly_fields = ['pub_date']
    inlines = [ChoiceInline]
    list_filter=['pub_date']    #django admin에서 제공하는 필터
    search_fields=['question_text', 'choice__choice_text']     #검색 기능

admin.site.register(Questions, QuestionAdmin)
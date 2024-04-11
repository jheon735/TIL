from django.urls import path
from .views import *

urlpatterns = [
    # path('question/', question_list, name='question-list'),
    path('question/', QuestionList.as_view(), name='question-list'),
    # path('question/<int:id>/', question_detail, name='question-detail'),
    # path('question/<int:id>/', QuestionDetail.as_view(), name='question-detail'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='question-detail'), #mixin 메서드 사용할 땐 pk로 받아온다
]
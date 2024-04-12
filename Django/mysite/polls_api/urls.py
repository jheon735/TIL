from django.urls import path, include
from .views import *

urlpatterns = [
    # path('question/', question_list, name='question-list'),
    path('question/', QuestionList.as_view(), name='question-list'),
    # path('question/<int:id>/', question_detail, name='question-detail'),
    # path('question/<int:id>/', QuestionDetail.as_view(), name='question-detail'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='question-detail'), #mixin 메서드 사용할 땐 pk로 받아온다
    path('users/', UserList.as_view(), name='user-list'),
    path('user/<int:pk>', UserDetail.as_view()),
    path('register/', RegisterUser.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('vote/', VoteList.as_view()),
    path('vote/<int:pk>', VoteDetail.as_view()),
]
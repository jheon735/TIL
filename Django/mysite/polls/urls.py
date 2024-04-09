from django.urls import path
from .  import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),    # 상위 url에서 타고 들어와서 하위 url이 없을 때 view.index로 보냄
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

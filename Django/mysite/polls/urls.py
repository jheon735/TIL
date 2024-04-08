from django.urls import path
from .  import views

urlpatterns = [
    path('', views.index, name='index'),    # 상위 url에서 타고 들어와서 하위 url이 없을 때 view.index로 보냄
    path('some_url', views.some_url),
]

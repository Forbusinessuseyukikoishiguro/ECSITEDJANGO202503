from django.urls import path
from . import views

app_name = 'template_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('sample1/', views.sample1, name='sample1'),  # 末尾にスラッシュを追加
    path('sample2/', views.sample1, name='sample2'), 
    path('sample/', views.sample, name='sample'),
]
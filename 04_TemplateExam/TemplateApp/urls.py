from django.urls import path
from.inport views

app_name = 'app'

urlpatterns = [
    path('home', views.home, name='index'),
    path('members', views.members, name='members'),
    path('member/<int:id>', views.member, name='member'),
]


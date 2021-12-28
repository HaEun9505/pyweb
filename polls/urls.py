from django.urls import path
from polls import views

app_name = 'poll'

urlpatterns = [
    #설문 조사 메인
    path('', views.index, name='index'),   #127.0.0.1:8000
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/vote/', views.vote, name='vote'),
]

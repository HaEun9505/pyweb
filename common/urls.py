from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'common'  #네임 스페이스 설정

urlpatterns = [
    #LoginView 클래스(제네릭 뷰)를 사용하면 제어함수를 만들지 않음
    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
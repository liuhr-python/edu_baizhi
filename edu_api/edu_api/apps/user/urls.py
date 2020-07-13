from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from user import views

urlpatterns = [
    path("login/", obtain_jwt_token),   # 登录生成token
    path("captcha/", views.CaptchaAPIView.as_view()),   # 登录核对验证条
    path("register/", views.UserAPIView.as_view()),     # 注册
    path("mobile/<str:mobile>", views.MobileCheckAPIView.as_view()),  # 检测手机号
    path("sms/<str:mobile>", views.SendMessageAPIView.as_view()),     # 手机验证码
]

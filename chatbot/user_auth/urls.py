from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/',views.LoginPage.as_view(),name="login"),
    path('reg/',views.RegisterPage.as_view(),name="register"),
    path('logout/',LogoutView.as_view(template_name="user_auth/logout.html"),name="logout"),
]


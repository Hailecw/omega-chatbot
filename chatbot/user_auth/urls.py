from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.LoginPage.as_view(),name="login"),
    path('reg/',views.RegisterPage.as_view(),name="register")
]
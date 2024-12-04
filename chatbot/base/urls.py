from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name="home"),
    path('<int:pk>/',views.TabDetailView.as_view(),name="tab-detail"),
]
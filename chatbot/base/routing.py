from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/home/conv/',consumers.AsyncChatbotConsumer.as_asgi())
]
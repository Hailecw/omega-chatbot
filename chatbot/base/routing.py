from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/home/conv/',consumers.AsyncChatbotConsumer.as_asgi()),
    path('ws/newtab/',consumers.NewTabConsumer.as_asgi()),
    path('ws/delete/',consumers.DeleteTabConsumer.as_asgi())
]
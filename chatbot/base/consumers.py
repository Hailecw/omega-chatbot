from channels.generic.websocket import AsyncWebsocketConsumer
import google.generativeai as genai
from base.models import MessagesModel,TabModel
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
import json


class AsyncChatbotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    async def receive(self, text_data):
        data = json.loads(text_data)
        user = await sync_to_async(User.objects.get)(username=self.scope['user'])
        u = await sync_to_async(MessagesModel.objects.create)(sender=user,msg=data['q'])
        tabs = await sync_to_async(TabModel.objects.filter)(user=user)
        last = await sync_to_async(tabs.last)()
        await sync_to_async(last.chats.add)(u)
        await sync_to_async(genai.configure)(api_key="AIzaSyBgHfH0Euc6hsfFzDl7Ara6ukS2z1Fl5jI")
        model = await sync_to_async(genai.GenerativeModel)("gemini-1.5-flash")
        response = await sync_to_async(model.generate_content)(data['q'])
        await self.send(json.dumps(response.text))
        o = await sync_to_async(MessagesModel.objects.create)(sender=await sync_to_async(User.objects.get)(username='omega'),msg=response.text)
        await sync_to_async(last.chats.add)(o)
        await self.send(json.dumps({'sender':'omega','a':response.text}))
from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer
import google.generativeai as genai
from base.models import MessagesModel,TabModel
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
import json
import markdown2


class AsyncChatbotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    async def receive(self, text_data):
        data = json.loads(text_data)
        user = await sync_to_async(User.objects.get)(username=self.scope['user'])
        u = await sync_to_async(MessagesModel.objects.create)(sender=user,msg=data['q'])
        tabs = await sync_to_async(TabModel.objects.filter)(user=user)
        last = await sync_to_async(tabs.last)()
        if not last:
            last = await sync_to_async(TabModel.objects.create)(user=user)
        if not last.title:
            last.title = data['q']
        await sync_to_async(last.save)()
        await sync_to_async(last.chats.add)(u)
        await sync_to_async(genai.configure)(api_key="AIzaSyBgHfH0Euc6hsfFzDl7Ara6ukS2z1Fl5jI")
        model = await sync_to_async(genai.GenerativeModel)("gemini-1.5-flash")
        response = await sync_to_async(model.generate_content)(data['q'])
        html_text = markdown2.markdown(response.text)
        await self.send(json.dumps(html_text))
        o = await sync_to_async(MessagesModel.objects.create)(sender=await sync_to_async(User.objects.get)(username='omega'),msg=html_text)
        await sync_to_async(last.chats.add)(o)
        await self.send(json.dumps({'sender':'omega','a':html_text,'title':data['q']}))

class NewTabConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        user = User.objects.get(username=self.scope['user'])
        TabModel.objects.create(user=user)
        self.disconnect()
class DeleteTabConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    def receive(self, text_data):
        id = int(json.loads(text_data))
        tab = TabModel.objects.get(id=id)
        tab.delete()
        self.disconnect('delete')




    
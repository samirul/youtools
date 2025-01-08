import json
import httpx
import requests
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class TaskStatus(AsyncWebsocketConsumer):
   def __init__(self):
        super().__init__(self)
        self.room_name = None
        self.room_group_name = None

   async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['task_id']
        self.room_group_name = 'task_%s' % self.room_name
        api_link = f"http://localhost:82/task_status/{self.room_name}/"
        req = requests.get(api_link, timeout=60)
        await (self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps(req.json()))

    
   async def receive(self, text_data=None, bytes_data=None):
       data = json.loads(text_data)
       await self.send(text_data=json.dumps(data))
       
#        data = json.loads(text_data)
#        auth_header = data.get('Authorization', '')
#        api_link = f"http://localhost:82/task_status/{self.room_name}/"
#        req = requests.get(api_link, headers={'Authorization': auth_header}, timeout=60)

#        await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 "type": "message",
#                 "message": json.dumps(req.json()),
#             }
#         )

    #    async with httpx.AsyncClient() as client:
    #     response = await client.get(api_link, headers={'Authorization': auth_header}, timeout=60)

        
 
   async def disconnect(self, code):
       await (self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
       
    
#    async def message(self, event):
#        data = json.loads(event.get('message'))
#        await self.send(text_data=json.dumps(data))
       
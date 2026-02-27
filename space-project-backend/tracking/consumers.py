import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ISSConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add("iss_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("iss_group", self.channel_name)

    async def send_iss_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))
        
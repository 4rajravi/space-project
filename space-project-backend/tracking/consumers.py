import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ISSConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.norad_id = self.scope["url_route"]["kwargs"]["norad_id"]

        self.group_name = f"sat_{self.norad_id}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_iss_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))
        
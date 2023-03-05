"""
    This file contains the code for webhook configurations
"""

import asyncio
import aiohttp
from discord import Webhook, File
from io import BytesIO

class WebhookHandler:
    async def send_webhook(self, webhook_url, image_path):
        async with aiohttp.ClientSession() as session:
            with open(image_path, 'rb') as f:
                image_data = f.read()
                webhook = Webhook.from_url(webhook_url, session=session)
                file = File(fp=BytesIO(image_data), filename='image.png')
                await webhook.send(file=file)
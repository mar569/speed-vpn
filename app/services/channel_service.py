import asyncio
from aiogram import Bot

class ChannelService:
    def __init__(self, bot: Bot, channel_id: str):
        self.bot = bot
        self.channel_id = channel_id

    async def post_to_channel(self, text: str):
        """Публикация сообщения в канал"""
        await self.bot.send_message(
            chat_id=self.channel_id,
            text=text
        )

    async def post_status(self, status: dict):
        """Публикация статуса серверов"""
        text = "📊 Статус серверов:\n"
        for server, info in status.items():
            text += f"{server}: {info}\n"
        await self.post_to_channel(text)
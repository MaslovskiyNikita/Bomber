from Bombers.telegram import telegram_bomb
from Bombers.VK import vk_bomb
from Bombers.A1 import A1_bomb
from Bombers.Dominos import Dominos_bomb
from Bombers.Zabava import Zabava_bomb
from Bombers.Rabota import Rabota_bomb
from Bombers.ok import ok_bomb
import asyncio
from os import getenv
from Consts import TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.methods import DeleteWebhook

token = getenv(TOKEN)
dp = Dispatcher()
bot = Bot(TOKEN)

@dp.message(CommandStart())
async def start(message: types.Message):
    if message.text == "/start":
        await bot.send_message(text="Скидывай номер c +375  ", chat_id=message.chat.id)

@dp.message()
async def Bombit(message: Message):
    while True:

        Zabava_bomb(message.text)
        A1_bomb(message.text)
        telegram_bomb(message.text)
        Dominos_bomb(message.text)
        vk_bomb(message.text)
        Rabota_bomb(message.text)
        ok_bomb(message.text)

async def main():
    await dp.start_polling(bot)
    await bot(DeleteWebhook(drop_pending_updates=True))

if __name__ == "__main__":
    asyncio.run(main())
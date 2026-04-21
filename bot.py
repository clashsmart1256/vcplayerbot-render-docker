import os
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text("Bot ready. Render pe successfully chal raha hai.")

@bot.on_message(filters.command("ping"))
async def ping(_, message: Message):
    await message.reply_text("pong")

bot.run()

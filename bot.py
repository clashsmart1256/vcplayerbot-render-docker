import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls, idle
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
SESSION_STRING = os.getenv("SESSION_STRING", "")

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client("user", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
calls = PyTgCalls(user)

@bot.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text("VC bot ready.")

@bot.on_message(filters.command("ping"))
async def ping(_, message: Message):
    await message.reply_text("pong")

@bot.on_message(filters.command("help"))
async def help_cmd(_, message: Message):
    await message.reply_text("/start
/ping
/play
/stop")

async def main():
    await bot.start()
    await user.start()
    await calls.start()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())

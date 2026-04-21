import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls, idle
import yt_dlp
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SESSION = os.environ.get("SESSION_STRING")

app = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client(":memory:", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)
pytgcalls = PyTgCalls(user)

@app.on_message(filters.command("start"))
async def start_cmd(client: Client, message: Message):
    await message.reply("VC Bot ready!
/play <YouTube URL> to start streaming.")

@app.on_message(filters.command("play") & filters.group)
async def play(client: Client, message: Message):
    link = message.text.split(maxsplit=1)[1]
    chat_id = message.chat.id
    
    ydl_opts = {'format': 'bestaudio', 'noplaylist': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=False)
        audio_file = ydl.prepare_filename(info)
    
    await pytgcalls.join_group_call(chat_id, audio_file)
    await message.reply(f"Playing: {info['title']}")

async def main():
    await app.start()
    await user.start()
    print("VC Bot deployed on Render! /play in group VC.")
    await pytgcalls.start()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())

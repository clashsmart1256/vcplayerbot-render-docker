import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
PORT = int(os.getenv("PORT", "10000"))

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

def run_web():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()

@bot.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text("Bot ready on Render.")

@bot.on_message(filters.command("ping"))
async def ping(_, message: Message):
    await message.reply_text("pong")

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    bot.run()


import pyrogram,os
from pyrogram import *
from pyrogram.types import *
import asyncio
from asyncio import *
import logging

APP_ID = int(26996374)
API_HASH = "12121c59e229974deb86532b788cd600"

app = Client("app", api_hash=API_HASH, api_id=APP_ID)


@app.on_message(filters.text & filters.chat(-1001613093650))
async def main_s(app, message):
 m_text = message.text
 await app.send_message(
  -1001819333581,
  text=f"""
{m_text}


@optrexchk
""",
  disable_web_page_preview=True,
 )

async def main_startup():
 try:
  print ("STARTING THE BOT...")
  await app.start()
  await idle()
 except Exception as e:
  print (e)

loop = asyncio.get_event_loop()
loop.run_until_complete(main_startup())

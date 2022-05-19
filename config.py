import os
import heroku3
from telethon import TelegramClient, events

from pyrogram import Client
from pyrogram import filters
import logging
#
# Burayı gurcalama
# 
# 
api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")

# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
USERNAME = os.environ.get("USERNAME")
group = int(os.environ.get("group"))
startmesaj = os.environ.get("startmesaj")
komutlar = os.environ.get("komutlar")
qrupstart = os.environ.get("qrupstart")
sahib = os.environ.get("sahib")
support = os.environ.get("support")
sahib = os.environ.get("sahib")
ozel_list = int(os.environ.get("ozel_list"))
#
app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )

import heroku3
import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation
from config import client, USERNAME, startmesaj, qrupstart, komutlar, sahib, support, group

from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
import time


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

anlik_calisan = []
tekli_calisan = []
ozel_list = [996686235, 1900050206]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**🐙 Octo Tagger Bot\nİle Grubunuzdaki Nerdeyse Tüm Üyelere Etiket Atabilirim \nKomutlar için ⇒ /help yazınız.**",
                    buttons=(
                   
		      [Button.url('Beni Grupa Ekle ➕', 'https://t.me/Etiketleme_bot?startgroup=a')],
                      [Button.url('Destek Grubu 🛠', 'https://t.me/OctopusGameDestek')],
                      [Button.url('Duyuru Kanalı 🐙', 'https://t.me/Octopus_Game')],
		      [Button.url('Developer 👨🏻‍💻', 'https://t.me/OctopusGameSahip')],
                    ),
                    link_preview=False
                   )

  if event.is_group:
    return await client.send_message(event.chat_id, f"**Beni Grubuna Aldığın için Teşekkürler ✨**")


@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Telegramdaki En Gelişmiş Üye Etiketleme Botu Octo Tagger Bot İle Grup Üyelerini Kolayca Etiketleyebilirsiniz. 🐙**\n\n**/tag - Üyeleri 7'li Şekilde Etiketler. ✅**\n\n**/soztag - Güzel Sözlerle Etiket Atar. ✅**\n\n**/isimtag Değişik İsimlerle Etiketler. ✅**\n\n**/futbol - Futbolcu İsimleriyle Etiketler. ✅**\n\n**/etag - Emojiler İle Etiketler. ✅**\n\n**/tektag - Üyeleri Tek Tek Etiketler. ✅**\n\n**/atag - Yöneticileri Etiketler. ✅**\n\n**/cancel - Etiketlemeyi Durdurur. ✅**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('Botu Gruba Ekle 👈', 'https://t.me/Etiketleme_bot?startgroup=a')],
                      [Button.url('Destek Grubu 👨‍💻', 'https://t.me/OctopusGameDestek')],
                      [Button.url('Duyuru Kanalı 🐙', 'https://t.me/Octopus_Game')],
		      [Button.url('Developer 🧑‍🔧', 'https://t.me/OctopusGameSahip')],
                    ),
                    link_preview=False
                   )
	
@client.on(events.NewMessage(pattern='^/reklam ?(.*)'))
async def duyuru(event):
 
  global grup_sayi,ozel_list
  sender = await event.get_sender()
  if sender.id not in ozel_list:
    return
  reply = await event.get_reply_message()
  await event.respond(f"Toplam {len(grup_sayi)} Gruba'a mesaj gönderiliyor...")
  for x in grup_sayi:
    try:
      await client.send_message(x,f"**{reply.message}**")
    except:
      pass
  await event.respond(f"Gönderildi.")
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla durduruldu.**\n\n**Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}")

@client.on(events.NewMessage())
async def mentionalladmin(event):
  global etiketuye
  if event.is_group:
    if event.chat_id in etiketuye:
      pass
    else:
      etiketuye.append(event.chat_id)


soz = [
'𝐾𝑎𝑙𝑏𝑖 𝑔ü𝑧𝑒𝑙 𝑜𝑙𝑎𝑛ı𝑛 𝑔ö𝑧ü𝑛𝑑𝑒𝑛 𝑦𝑎ş 𝑒𝑘𝑠𝑖𝑘 𝑜𝑙𝑚𝑎𝑧𝑚ış', 
'İ𝑦𝑖𝑦𝑖𝑚 𝑑𝑒𝑠𝑒𝑚 𝑖𝑛𝑎𝑛𝑎𝑐𝑎𝑘 𝑜 𝑘𝑎𝑑𝑎𝑟 ℎ𝑎𝑏𝑒𝑟𝑠𝑖𝑧 𝑏𝑒𝑛𝑑𝑒𝑛', 
'𝑀𝑒𝑠𝑎𝑓𝑒𝑙𝑒𝑟 𝑈𝑚𝑟𝑢𝑚𝑑𝑎 𝐷𝑒ğ𝑖𝑙, İç𝑖𝑚𝑑𝑒 𝐸𝑛 𝐺ü𝑧𝑒𝑙 𝑌𝑒𝑟𝑑𝑒𝑠𝑖𝑛',
'𝐵𝑖𝑟 𝑀𝑢𝑐𝑖𝑧𝑒𝑦𝑒 İℎ𝑡𝑖𝑦𝑎𝑐ı𝑚 𝑉𝑎𝑟𝑑ı 𝐻𝑎𝑦𝑎𝑡 𝑆𝑒𝑛𝑖 𝐾𝑎𝑟şı𝑚𝑎 Çı𝑘𝑎𝑟𝑑ı', 
'Ö𝑦𝑙𝑒 𝑔ü𝑧𝑒𝑙 𝑏𝑎𝑘𝑡ı 𝑘𝑖 𝑘𝑎𝑙𝑏𝑖 𝑑𝑒 𝑔ü𝑙üşü𝑛 𝑘𝑎𝑑𝑎𝑟 𝑔ü𝑧𝑒𝑙 𝑠𝑎𝑛𝑚ış𝑡ı𝑚', 
'𝐻𝑎𝑦𝑎𝑡 𝑛𝑒 𝑔𝑖𝑑𝑒𝑛𝑖 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟 𝑛𝑒 𝑑𝑒 𝑘𝑎𝑦𝑏𝑒𝑡𝑡𝑖ğ𝑖𝑛 𝑧𝑎𝑚𝑎𝑛ı 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟', 
'𝑆𝑒𝑣𝑚𝑒𝑘 𝑖ç𝑖𝑛 𝑠𝑒𝑏𝑒𝑝 𝑎𝑟𝑎𝑚𝑎𝑑ı𝑚 ℎ𝑖ç 𝑠𝑒𝑠𝑖 𝑦𝑒𝑡𝑡𝑖 𝑘𝑎𝑙𝑏𝑖𝑚𝑒', 
'𝑀𝑢𝑡𝑙𝑢𝑦𝑢𝑚 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑒𝑛𝑙𝑒', 
'𝐵𝑒𝑛 ℎ𝑒𝑝 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘 𝑖𝑠𝑡𝑒𝑑𝑖ğ𝑖𝑚 𝑔𝑖𝑏𝑖 𝑠𝑒𝑣𝑖𝑛𝑑𝑖𝑚', 
'𝐵𝑖𝑟𝑖 𝑣𝑎𝑟 𝑛𝑒 ö𝑧𝑙𝑒𝑚𝑒𝑘𝑡𝑒𝑛 𝑦𝑜𝑟𝑢𝑙𝑑𝑢𝑚 𝑛𝑒 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛', 
'Ç𝑜𝑘 𝑧𝑜𝑟 𝑏𝑒 𝑠𝑒𝑛𝑖 𝑠𝑒𝑣𝑚𝑒𝑦𝑒𝑛 𝑏𝑖𝑟𝑖𝑛𝑒 𝑎şı𝑘 𝑜𝑙𝑚𝑎𝑘', 
'Ç𝑜𝑘 ö𝑛𝑒𝑚𝑠𝑒𝑑𝑖𝑘 𝑖ş𝑒 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡ı𝑘 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑦𝑜𝑟𝑢𝑧', 
'𝐻𝑒𝑟𝑘𝑒𝑠𝑖𝑛 𝑏𝑖𝑟 𝑔𝑒ç𝑚𝑖ş𝑖 𝑣𝑎𝑟, 𝐵𝑖𝑟𝑑𝑒 𝑣𝑎𝑧𝑔𝑒ç𝑚𝑖ş𝑖', 
'𝐴şı𝑘 𝑜𝑙𝑚𝑎𝑘 𝑔ü𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑎𝑛𝑎', 
'𝐴𝑛𝑙𝑎𝑦𝑎𝑛 𝑦𝑜𝑘𝑡𝑢, 𝑆𝑢𝑠𝑚𝑎𝑦ı 𝑡𝑒𝑟𝑐𝑖ℎ 𝑒𝑡𝑡𝑖𝑚', 
'𝑆𝑒𝑛 ç𝑜𝑘 𝑠𝑒𝑣 𝑑𝑒 𝑏ı𝑟𝑎𝑘ı𝑝 𝑔𝑖𝑑𝑒𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛', 
'𝑂 𝑔𝑖𝑡𝑡𝑖𝑘𝑡𝑒𝑛 𝑠𝑜𝑛𝑟𝑎 𝑔𝑒𝑐𝑒𝑚 𝑔ü𝑛𝑑ü𝑧𝑒 ℎ𝑎𝑠𝑟𝑒𝑡 𝑘𝑎𝑙𝑑ı', 
'𝐻𝑒𝑟 ş𝑒𝑦𝑖𝑛 𝑏𝑖𝑡𝑡𝑖ğ𝑖 𝑦𝑒𝑟𝑑𝑒 𝑏𝑒𝑛𝑑𝑒 𝑏𝑖𝑡𝑡𝑖𝑚 𝑑𝑒ğ𝑖ş𝑡𝑖𝑛 𝑑𝑖𝑦𝑒𝑛𝑙𝑒𝑟𝑖𝑛 𝑒𝑠𝑖𝑟𝑖𝑦𝑖𝑚', 
'𝐺ü𝑣𝑒𝑛𝑚𝑒𝑘 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛 𝑑𝑎ℎ𝑎 𝑑𝑒ğ𝑒𝑟𝑙𝑖, 𝑍𝑎𝑚𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎𝑟𝑠ı𝑛', 
'İ𝑛𝑠𝑎𝑛 𝑏𝑎𝑧𝑒𝑛 𝑏ü𝑦ü𝑘 ℎ𝑎𝑦𝑒𝑙𝑙𝑒𝑟𝑖𝑛𝑖 𝑘üçü𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑𝑒𝑟', 
'𝐾𝑖𝑚𝑠𝑒 𝑘𝑖𝑚𝑠𝑒𝑦𝑖 𝑘𝑎𝑦𝑏𝑒𝑡𝑚𝑒𝑧 𝑔𝑖𝑑𝑒𝑛 𝑏𝑎ş𝑘𝑎𝑠ı𝑛ı 𝑏𝑢𝑙𝑢𝑟, 𝑘𝑎𝑙𝑎𝑛 𝑘𝑒𝑛𝑑𝑖𝑛𝑖', 
'𝐺üç𝑙ü 𝑔ö𝑟ü𝑛𝑒𝑏𝑖𝑙𝑖𝑟𝑖𝑚 𝑎𝑚𝑎 𝑖𝑛𝑎𝑛 𝑏𝑎𝑛𝑎 𝑦𝑜𝑟𝑔𝑢𝑛𝑢𝑚', 
'Ö𝑚𝑟ü𝑛ü𝑧ü 𝑠𝑢𝑠𝑡𝑢𝑘𝑙𝑎𝑟ı𝑛ı𝑧ı 𝑑𝑢𝑦𝑎𝑛  𝑏𝑖𝑟𝑖𝑦𝑙𝑒 𝑔𝑒ç𝑖𝑟𝑖𝑛', 
'𝐻𝑎𝑦𝑎𝑡 𝑖𝑙𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘ı𝑙𝑎𝑟𝑎𝑘 𝑦𝑎ş𝑎𝑛ı𝑟 𝑔𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘𝑎𝑟𝑎𝑘 𝑎𝑛𝑙𝑎şı𝑙ı𝑟', 
'𝐴𝑟𝑡ı𝑘 ℎ𝑖ç𝑏𝑖𝑟 ş𝑒𝑦 𝑒𝑠𝑘𝑖𝑠𝑖 𝑔𝑖𝑏𝑖 𝑑𝑒ğ𝑖𝑙 𝐵𝑢𝑛𝑎 𝑏𝑒𝑛𝑑𝑒 𝑑𝑎ℎ𝑖𝑙𝑖𝑚', 
'𝐾ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛𝑒 𝑔ö𝑛ü𝑙𝑑𝑒 𝑣𝑒𝑟𝑖𝑙𝑖𝑟 ö𝑚ü𝑟𝑑𝑒', 
'𝐵𝑖𝑟 ç𝑖ç𝑒𝑘𝑙𝑒 𝑔ü𝑙𝑒𝑟 𝑘𝑎𝑑ı𝑛 𝑏𝑖𝑟 𝑙𝑎𝑓𝑙𝑎 ℎü𝑧ü𝑛', 
'𝑈𝑠𝑙ü𝑝 𝑘𝑎𝑟𝑎𝑘𝑡𝑒𝑟𝑖𝑑𝑖𝑟 𝑖𝑛𝑠𝑎𝑛ı𝑛', 
'𝐻𝑒𝑟 ş𝑒𝑦𝑖 𝑏𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑖𝑙 𝑘ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟 𝑜𝑙𝑠𝑢𝑛 ℎ𝑎𝑦𝑎𝑡ı𝑛ı𝑧𝑑𝑎', 
'𝑀𝑒𝑠𝑎𝑓𝑒 𝑖𝑦𝑖𝑑𝑖𝑟 𝑁𝑒 ℎ𝑎𝑑𝑑𝑖𝑛𝑖 𝑎ş𝑎𝑛 𝑜𝑙𝑢𝑟 𝑛𝑒 𝑑𝑒 𝑐𝑎𝑛ı𝑛ı 𝑠ı𝑘𝑎𝑛', 
'𝑌ü𝑟𝑒ğ𝑖𝑚𝑖𝑛 𝑡𝑎𝑚 𝑜𝑟𝑡𝑎𝑠ı𝑛𝑑𝑎 𝑏ü𝑦ü𝑘 𝑏𝑖𝑟 𝑦𝑜𝑟𝑔𝑢𝑛𝑙𝑢𝑘 𝑣𝑎𝑟', 
'𝑉𝑒𝑟𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑒𝑟𝑖𝑛 𝑛𝑎𝑛𝑘ö𝑟ü 𝑜𝑙𝑚𝑎𝑦ı𝑛 𝑔𝑒𝑟𝑖𝑠𝑖 ℎ𝑎𝑙𝑙𝑜𝑙𝑢𝑟', 
'𝐻𝑒𝑚 𝑔üç𝑙ü 𝑜𝑙𝑢𝑝 ℎ𝑒𝑚 ℎ𝑎𝑠𝑠𝑎𝑠 𝑘𝑎𝑙𝑝𝑙𝑖 𝑏𝑖𝑟𝑖 𝑜𝑙𝑚𝑎𝑘 ç𝑜𝑘 𝑧𝑜𝑟', 
'𝑀𝑢ℎ𝑡𝑎ç 𝑘𝑎𝑙ı𝑛 𝑦ü𝑟𝑒ğ𝑖 𝑔ü𝑧𝑒𝑙 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑎', 
'İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣𝑒 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖ç𝑒𝑘 𝑎ç𝑎𝑟', 
'İ𝑠𝑡𝑒𝑦𝑒𝑛 𝑑𝑎ğ𝑙𝑎𝑟ı 𝑎ş𝑎𝑟 𝑖𝑠𝑡𝑒𝑚𝑒𝑦𝑒𝑛 𝑡ü𝑚𝑠𝑒ğ𝑖 𝑏𝑖𝑙𝑒 𝑔𝑒ç𝑒𝑚𝑒𝑧', 
'İ𝑛ş𝑎𝑙𝑙𝑎ℎ 𝑠𝑎𝑏ı𝑟𝑙𝑎 𝑏𝑒𝑘𝑙𝑒𝑑𝑖ğ𝑖𝑛 ş𝑒𝑦 𝑖ç𝑖𝑛 ℎ𝑎𝑦ı𝑟𝑙ı 𝑏𝑖𝑟 ℎ𝑎𝑏𝑒𝑟 𝑎𝑙ı𝑟𝑠ı𝑛', 
'İ𝑦𝑖 𝑜𝑙𝑎𝑛 𝑘𝑎𝑦𝑏𝑒𝑡𝑠𝑒 𝑑𝑒 𝑘𝑎𝑧𝑎𝑛ı𝑟', 
'𝐺ö𝑛𝑙ü𝑛ü𝑧𝑒 𝑎𝑙𝑑ığı𝑛ı𝑧 𝑔ö𝑛𝑙ü𝑛ü𝑧ü 𝑎𝑙𝑚𝑎𝑦ı 𝑏𝑖𝑙𝑠𝑖𝑛', 
'𝑌𝑖𝑛𝑒 𝑦ı𝑟𝑡ı𝑘 𝑐𝑒𝑏𝑖𝑚𝑒 𝑘𝑜𝑦𝑚𝑢ş𝑢𝑚 𝑢𝑚𝑢𝑑𝑢', 
'Ö𝑙𝑚𝑒𝑘 𝐵𝑖 ş𝑒𝑦 𝑑𝑒ğ𝑖𝑙 𝑦𝑎ş𝑎𝑚𝑎𝑚𝑎𝑘 𝑘𝑜𝑟𝑘𝑢𝑛ç', 
'𝑁𝑒 𝑖ç𝑖𝑚𝑑𝑒𝑘𝑖 𝑠𝑜𝑘𝑎𝑘𝑙𝑎𝑟𝑎 𝑠ığ𝑎𝑏𝑖𝑙𝑑𝑖𝑚 𝑁𝑒 𝑑𝑒 𝑑ış𝑎𝑟ı𝑑𝑎𝑘𝑖 𝑑ü𝑛𝑦𝑎𝑦𝑎', 
'İ𝑛𝑠𝑎𝑛 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘𝑡𝑒𝑛 ç𝑜𝑘 𝑎𝑛𝑙𝑎şı𝑙𝑚𝑎𝑦ı 𝑖𝑠𝑡𝑖𝑦𝑜𝑟𝑑𝑢 𝑏𝑒𝑙𝑘𝑖 𝑑𝑒', 
'𝐸𝑘𝑚𝑒𝑘 𝑝𝑎ℎ𝑎𝑙ı 𝑒𝑚𝑒𝑘 𝑢𝑐𝑢𝑧𝑑𝑢', 
'𝑆𝑎𝑣𝑎ş𝑚𝑎𝑦ı 𝑏ı𝑟𝑎𝑘ı𝑦𝑜𝑟𝑢𝑚 𝑏𝑢𝑛𝑢 𝑣𝑒𝑑𝑎 𝑠𝑎𝑦',
"Biz mi İZ'in peşinden koşarız yoksa İZ mi bizi kovalar?", 'Şaşırmayınız, bu toplum zamanı kullanma özürlüdür.', 'Günlerin bir akşamının olması, nasıl da acımasızdı!', 'Sen onu yaralarından tanıdın, O sana yarasını açmadı.', 'Ten dikenliğinden geçmeden, can gülistanına varamazsın.', 'O günden sonra bildiğimi unuttum, unutarak yeniden bildim.', 'Senin var olduğunu bilmek yaşamaya devam etmemin sebebiydi', 'Mektuplar ruhları öpücüklerden daha çok kaynaştırır.', 'Belki de gerçek, iki çocuk arasındaki en kısa doğrudur.', 'Ona koşmak ve aynı zamanda da ondan uzaklaşmak istiyorum.', 'Hırs, tırnakları çıkarır ama ayaklara da taş bağlar.', 'Ne kadar derine yuvarlanırsan, o kadar yükseğe uçarsın.', 'Gözler yaşarmadıkça gönüllerde gökkuşağı oluşmaz.', 'Gözlerimi yaklaşan sonuma dikip huzur içinde yaşıyorum.', 'Aşk, yaşamı; cinayet, ölümü sıradanlıktan kurtarır.', 'Bazı şeyleri yarım bileceğine, bir şey bilme, daha iyi.', 'Biz buğdayı evcilleşirmedik, buğday bizi evcilleştirdi.', 'Dünyanın bana ait olduğunu sandığım zamanlar olmuştu.', 'Hasta düşünceler gibi hayaller üretiyorlar kafalarında.', 'İnsanın adaleti araması için illa bir sebebi mi olmalı?', 'Hayat güzel olabilir. Uğrunda mücadele etmeye değebilir.', 'Arkadaş sahibi olmanın tek yolu, önce arkadaş olmaktır.', 'Yaşamın amacı karşıtlıklar arasında denge kurmaktır.', 'İnsan güzel bir kitap okuduğu yerden nasıl ayrılabilir?', 'Hiçbir yere gitmiyorsun. Tam da olman gerektiğin yerdesin!', 'Yetenek yapabileceğini yapar, deha ise yapması gerekeni.', 'Gemi kullanmayı öğrenmek için fırtınalardan korkmam.', 'Bu bir tabiat kanunuydu: Kuvvetliler zayıfları eziyordu.', 'Her şeye vakit vardır ama yapmaya değer şeyler hariç.', 'Düşüncelerin seni ne geleceğe ne de geçmişe taşır.', 'Bilinç yalnızca sen hiçbir yere gitmiyorken berraktır.', 'Camus bir ideoloji adına yaratılan şiddete karşıydı.', 'Şimdi artık çok geç. Zaten her zaman çok geç olacak.', 'Gülmeyle her şey öldürülebilirdi, hatta cinayet bile.', 'Hangi sevdanın yuvasından atılmış leylek yavrusuydum.', 'Hayatımda bana ait olmayan bir zaman yaşamaya başladım', "Bizim tek ulu önderimiz vardır, o da YÜCE ATATÜRK'tür. ", 'Çünkü hayat ne geriye gider ne de geçmişle ilgiklenir', 'Savaş alanı da insanlar için en büyük ibret okuludur.', 'Sevmeyi öğreneceksiniz, dinlemeyi öğrendiğiniz zaman.', 'Aşk, mert işidir. Mertliğin de kadını erkeği yoktur.', 'Bu aralar daha çok okumalıyım, yoksa hüzünleneceğim.', 'Az ümit edip çok elde etmek hayatın hakiki sırrıdır.', 'Edepli edebinden susar, edepsiz de ben susturdum zanneder.', 'Sokaklardaki insanların o bakışları içime işliyordu.', 'Ben senden başkasını görmüyorum ki baktığım yerde.', 'Burası bizim değil, bizi öldürmek isteyenlerin ülkesi!', 'Erkeğin eşini öldürdüğü tek hayvan türü insandır.', 'Değer verin ya da vermeyin, ama asla verir gibi yapmayın.', 'Onurlu bir adam, susuzluğunu giderdiği kuyuya taş atmaz.', 'Güzel kadınları hayal gücü olmayan erkeklere bırakın', 'Kurnazlığın, hilenin olduğu yerde küçüklük vardır.', 'Görmezden gelinmek, alaya alınmaktan da kötü bir histi.', 'Bazı erkekler ancak seçenekleri ölçüsünde sadıktır.', 'Yerinde duran, geriye gidiyor demektir İleri, daima ileri!', "Çağın vebası: 'mutsuz insanlar', 'mutlu fotoğraflar’", 'Belden aşağısı bedenin aşkı, belden yukarısı ruhun.', 'Hayatın saldırılarına karşı bir savunmadır edebiyat.', 'Derin düşünceler, derin sessizlik gerektirir.', 'İlk izlenim daima hayal kırıklığı yaratır', 'İki soylu kavga edince fakirin kulübesi yanar.', 'Elimi şah damarıma koydum ama gülümsüyordum', 'Kitaplar başka yerde olmak isteyenler içindir.', 'İyi iştah vicdanın rahatlığına işarettir.', 'Hayat bir şey değildir, itinayla yaşayınız.', 'Korkularınızdan saklanmak onları yok etmezdi.', 'Can gövdeye yük, dünya insana mülk değildir', 'Sevilen nesne kem gözlerden sakınılmalıdır.', 'İnsan mezardan dönemez ama hatadan dönebilir.', 'Gece açılıp gündüz kapanan bir parantezdim.', 'Bir çocuk en çok başka bir çocuğa güvenir.', 'Bazen insanlardan çok hikâyeleri etkiler sizi.', 'Acı bazı insanların anladıkları tek dildir.', 'Geçmişin güzelliği geçmiş olmasındandır.', 'Namazda gözü olmayanın kulağı ezanda olmaz.', 'Çok canım sıkılıyor, kuş vuralım istersen', 'Terbiyenin sırrı, çocuğa saygı ile başlar.', 'Ölüm hayatın sonu değil , bir aşamasıdır.', 'Kendini beğenmişler yalnız övgüleri dinler.', 'Ey kutsal gece! Sen de bizden haz alır mısın?', 'İşte bağırıyorum. Ve beni duyan gene benim.', 'Yıllar uçup gider ama kalp aynı yerde kalır.', 'Rüzgarla gelen babam, yine rüzgarla gitmişti.', "Uyumak, ölmeye yatmak demekti Sarıkamış' ta.", 'Balıkçıyla evlenmek denizle evlenmek gibidir.', 'Bütün yapraklarını dökmüş bir orman kadar bitkindim.', 'Marifet tadı alarak yaşamakta. Bazen akıllı, bazen deli', 'Aşırı kızgınlığın verdiği bir sakinlik içindeydi.', 'Düşünce değerli bir şeydi, sonuçlar veren bir şeydi.', 'İnsanı olgunlaştıran yaşı değil, yaşadıklarıdır.', 'İnsan ancak bir başkasının varlığıyla anlam buluyor.', 'Sensizliğin, sürekli seni hatırlatmasından bahsediyorum', 'Güç insanı bozar. Ve mutlak güç insanı mutlaka bozar.', 'Ah! İnsanın insandan vazgeçemediği nasıl da doğruydu.', 'Her uygarlık teokrasi ile başlayıp demokrasiye ulaşır.', 'Kibir tamamen sona erdiğinde alçakgönüllülük başlar.', 'Kitaplar yaşadıkça geçmiş diye bir şey olmayacaktır.', 'Adalet ancak gerçekten, saadet ancak adaletten doğabilir.', 'Merhamet yararsız olduğu zaman insan merhametten yorulur.', 'Kendini okumayan benim alfabemi bilemez, beni de anlayamaz.', 'Yaprakların düşerken attıkları çığlıkları duydum.', 'Aldığım nefesten bile daha çok ihtiyaç duyuyordum ona.', 'Her emir özgürlüğün suratında patlayan bir tokattır.', 'Efendim, mutlu olmak için mutlaka zengin mi olmak gerekir?', 'Belleğin seni en çok etkileyen şeyleri en derine saklar.', 'Hırsızlardan en zararlısı zamanınızdan çalanlardır.', 'Tay at olunca at dinlenir, çocuk adam olunca ata dinlenir.', 'İmkansız olanı yapamasam da, elimden geleni yapacağım.', 'Önüne gelenle değil, seninle ölüme gelenle beraber ol.', 'İnsanların zamanına hükmedenin gücü sınırsız olur.', 'Karşılıksız bir aşk kadar acımasız bir kader yoktur.', 'Odunu fazla inceltmeye kalkarsan, kıymık olup sana batar.', 'Dünya boşunalığa gebe kalmış ve zulmü doğurmuştur.', 'Keşke gerçek hayat resimlerdeki kadar mükemmel olsaydı.', 'İnsan eliyle ölümler artık bana katlanılmaz geliyordu.', 'Kabul etmesi çok zordu ama yıllar çok çabuk geçiyordu.', 'Ölümünüz, çalamayacağınız ilk fotoğraf olacaktır.', 'Yerimizi boşaltsak da dünyaya yeni geleceklere yer açsak', 'İnsanlar iyi giyimli. Ama içlerinde soluk yok. Soluk yok.', 'Hayır, rüzgarın dilinde her mevsim aynı şarkı yoktur.', 'En hüzünlü kuşlar bile şakıyacak bir mevsim bulurlar.', 'Gelmeyeceğini bile bile beklemek saflık değil, aşktır!', 'Aşk denen şey kafanda tanım değiştirince canın yanar.', 'Neden gençliğimde kitap okumadım? diye kendime kızdım.', 'Açlık insanı öldüren, partileri yaşatan bir olaydır.', 'İnsan ömrü, unutmanın şerbetine yiyecek kadar muhtaç.', 'Öfkenin başlangıcı çılgınlık, sonu pişmanlıktır.', 'Belki de bu evren, yüce bir ruhun gölgesidir.', 'Konuşmak dilin işi değil kalbin marifetidir.', 'Erdem eken onu sık sık sulamayı unutmamalı.', 'Kıskancın suskunluğu çok gürültülüdür.', 'Karşılaştığı olayları ikiye ayırıyordu', 'Bir kadının hayatta aldığı en büyük risk', 'Tecrübe insanın başına gelen şey değildir', 'Mucizeler bir kere başladı mı bitmek bilmez!', 'İnsan mı egosunu, egosu mu insanı kullanır?', 'Şiirin amacı, bizi şiir haline sokmasıdır.', 'Kadınlar da her şey tenlerinin altına işler', 'Hayır, Jamie. Ben daha zenginim. Sana sahibim.', 'İtfaiye ile ateş arasında tarafsız kalamam.', 'Gördüğünü sandığın şeyi görmüyorsun.', 'Duygularım sevgi değil , sevgiden daha özel.', 'Acaba ölsem beni daha mı çok severler belki?', 'Dostumuz bilge olamayacak kadar kurnaz biridir.', 'Göreceksin ki hayatın zevki değişikliktedir', 'Beni anlasa, o da benimle aynı düşü görse!', 'Burada bir aşık vardı maşuğuna kanatlandı', 'İtip beni, balıma dadanan bu çağı sevmedim', 'Ama sen fikirleri seviyorsun insanları değil.', 'Yukarıdan bakmak, yukarı bakmaktan kolaydır.', 'Hiçbir şey yapmadan geçen hayat, ölümdür.', '0 ile 100 arasındaki 10 saniyelik süre bitti.', 'Benim güzel çocukluğumu ahmak bir ayak ezdi.', 'Hatıralar durmaksızın hücum ediyor zihnime.', 'Başarısızlık, başarmamış olmak demektir. Gerçekten öyle', 'Aşk bir çeşit zafer yürüyüşü değildir.', 'İnsan elinde olmayan şeyleri düşünür hep.', 'Unutma! Gönül zengini, cebine zaman ayırmaz.', 'Biz dünyadan gider olduk kalanlara selam olsun', 'Onun kara gözlerini görmek bile bana yetiyor.', 'Ulan bu canım memlekette ya kudura kudura ölecez ya da delire delire!', 'Her işin bir vakti vardır. Vakti geçince o işten hayır beklenemez.', 'Düşüncelerimizde ne barındırırsak deneyimlerimizde onu yaşarız.', 'İnsan gurura kapılmamalıdır, aciz ve zavallı olduğunu bilmelidir.', 'Tüm kaosta bir kozmos ve tüm düzensizlikte gizli bir düzen vardır.', 'Bazen vicdani yargı, idamdan daha ağır bedeller ödetebilirdi insana', 'Verdiğin bütün acılara dayanabiliyorsam , seni özlediğim içindir', 'İçimdeki seni beğenmiyorsan. İçime karışma! Sen kendi içine bak', 'Hayallerinizdeki ağacı, siz izin vermeden kesmeye kimin gücü yeter?', 'Hayatta fevkalade hiçbir hadise yoktur. Her şey birbirinin aynıdır.', 'Yaşam, insan zihninin icat edebileceği her şeyden kat kat tuhaftır.', 'Kalbimiz bir hazinedir, onu birden boşaltınız, mahvolmuş olursunuz.', 'İnsandan ve eşyadan azaldıkça, sevgiden ve huzurdan çoğalırsın.', 'Ve o gün öyle bir gittin ki, ben o günden sonra kendimi hissetmedim.', '"Zekâ; fikirlerle uğraşırken, akıl; sistemli düşünceye yönelir!"', 'Radyasyondan çok birbirlerinin kalplerini kırmaktan ölüyor insanlar', 'Ama asla anlayamadım olup biteni. Anlaşılır şey de değildi zaten.', 'Gerçek değişimin kanıtlanmaya ihtiyacı yoktur Değişirsin, biter.', 'Gelecek ne zaman vaat olmaktan çıkıp bir tehdit unsuru haline geldi?', 'Bir toplum ne kadar özgür olursa, güç kullanmak o kadar zorlaşır.', 'Sefaletin son derecesindeki insan az bir şeyle kendini zengin görür.', 'Bir de vatan denen bir şey vardı ki, çok iyi korunması gerekiyordu.', 'Gözlerindeki yumuşamadan anlıyordum ki, becerebilseydi gülümserdi.', 'Fırtınaya hiç yakalanmamış bir gemi, limanda yapayalnız demektir.', 'Sıfırı sıfırla bin kez de çarpsanız yine sıfır elde edersiniz! Sıfır üzeri sonsuz hariç.', 'Bir dili bilmek dendiği zaman, o dilde düşünebilmektir aklıma gelen.', 'Aşkın arzusuna ulaşmasını engelleyen şey yine aşkın kendisiydi.', 'Bazı yaralar vardır ki, kapanmış olsalar bile dokununca sızlarlar.', 'Bedenim iyileşebileceği, ama ruhumun yaraları asla iyileşmeyecekti.', 'Çünkü aylaklık yeryüzünün mevsimlerine yabancılaşmak demektir.', "Regan'ın adam olacağı zaten daha küçücük bir çocukken belliydi.", 'Yaşamak bir denge meselesi. Birine aşırı bağlanmak dengesizliktir.', 'Ve daima duyarım zaman denen kanatlı arabanın arkamdan gelen sesini.', 'Günümüz insanlarının problemi, kendilerini fazla ciddiye almaları.', 'Buz kadar lekesiz, kar kadar temiz olsan bile, iftiradan kurtulamazsın.', 'Dokunur işte Kalemin ucu kağıda, kağıtta yazılanların ucu da bana', 'Anlamayacak olanlara söyleme sakın, bilebileceğin en güzel şeyleri!', 'Bir bavula her şey sığmadıkça gitmek hiçbir zaman kolay olmayacak.', 'Adaletin ne olduğundan habersiz bir insan adalet üzerine ne yazabilir?', 'Mezardakilerin pişman oldukları şeyler için diriler birbirini yiyor.', 'Ama işte hayat böyle: Ne fazla şikayetçi ol, ne de fazla beklentili.', 'İnsanlar yalnız felaketi yaşarken gerçeğe kendilerini kaptırırlar', 'Bana hakaret ederek kendi kusurlarını örtebileceğini mi sanıyorsun?', 'Türkçe hocasına göre, çoğul konuşanlar alçakgönüllü olurmuş.', 'Sen, ağaca bakmaktan ormanı göremeyen o küçük insanlardan birisin.', 'Ve insanların arasında yalnız olmaktan daha korkunç bir şey yoktur.', 'Nefret ettikleriniz bile gittiğinde içinizde bir boşluk bırakırlar.', 'Bazı durumlarda insanın rahatça ağlayabilmesi bile bir nimet oluyor.', '"İki güçlü savaşçı vardır, bunlar sabır ve zamandır.', 'De bana, her şeye sahip birine gönderilecek en isabetli hediye nedir?', 'Sarayın bahçesindeki maymunlar gibiydi zihni. Daldan dala atlıyordu.', 'Kaybedecek hiç bir şeyi olmayanların bomboş gözleriyle bakıyorsun', 'İnsanı anlamakla meşgulüz, üstelik görünürde hiç ipucu da yok.', 'Egemenlik gerçekten milletin olduğunda hükümetlere gerek kalmayacak', 'Hikayesi yok, diyorum. Bir gün seni gördüm ve öylece anlayıverdim.', 'Bütün gördüğümüz ve göründüğümüz, düş içinde bir düş.', 'Kaybolmuş bir ruhum var. Yorgun ama artık umutlu o umut sensin Kayla.', 'Fakat yüreğimdeki gizli yaralar vücudumdakilerden çok daha derindi.', 'Dikkat ettin mi, bugünlerde insanlar birbirlerini nasıl incitiyorlar.', 'Değişmeniz için önemli bir şeylerin risk altında olması gerekir.', 'Yalnızdım, çünkü acı sadece tek kişilikti. Korku tek kişilikti.', 'Okurlara vasat, verimli yanlarımı gösterseydim, bir servetim olurdu.', 'Kimse sizi öğrenmeye zorlayamaz. Siz istediğinizde öğreneceksiniz.', 'Ve yine de sefil yasalar ve sefil insanlar, ben kötü biri değildim !', 'İnsanın hayatı kendi eseridir. Herkes kendi hayatının mimarıdır.', 'Kalıbına yakışanı arar durursan. Kalbine yakışanı zor bulursun!', 'Hangisi daha kötü: Sevmeden sevişmek mi yoksa sevişmeden sevmek mi?', 'Birkaç gün sonra her şey bitti. Yaşamaya hükümlüydüm. Yasamaya!', 'İyi de, kör olmak ölmek değil ki, Evet ama ölmek kör olmak demek.', 'Dorukta yalnız kalmaktan ve doruktan başlamak ne kadar zormuş meğer', 'Acıyla yaşamanın mümkün olduğunu sen herkesten daha iyi bilirsin.', 'Her şey hüküm sürmekle ilgiliyse, bırakın isyan hüküm sürsün.', 'Kendisiyle ilgili bir olayda da adil bir yargılayıcı olabilir miydi?', 'Annemiz, ışınları artık ısıtmayan örtülü bir güneş gibiydi.', 'Kuralların dışına çıkan bir adam, muteber birisi değil demektir.', 'Doğru yoldan giden topal, yoldan sapan çabuk yürüyüşlüyü geçer', 'Şiddet ahlak seviyesi düşük erkeklere her zaman çekici gelmiştir.', 'Artık her şey gece. Sonuna kadar gece. Sonsuz gece. Sonsuz karanlık.', 'Samimiyetin lisanı yoktur. O, gözlerden ve tavırlardan anlaşılır.', 'Kitap, müzik, meditasyon ve arkadaş, ruhumuza en iyi gelen tedavidir.', 'Kesinlikle bilmeniz gereken tek şey, kütüphanenin nerede olduğudur.', 'Bugün de bir şey olmadı. O olmayan şey her neyse, onu özlüyordum.', 'Hayat gerçekten basit ama biz karmaşıklaştırmakta ısrar ediyoruz.', 'Her birimiz geçici olmanın tutkuyla karışık acıklı itirafıyız.', 'İnsan mı paraya bağlı, para mı insana bağlı? Bu, insana bağlı.', 'Hayattan pek çok şey öğrenen insanlar, neşeli ve masum kalamazlar.', 'Birisinin zengin olması için diğerinin fakirleşmesine gerek yoktur.', 'Senden ayrılınca anımsadım dünyanın bu kadar kalabalık olduğunu', 'Bana öyle geliyor ki sen de beni seviyorsun, ya da bana öyle geliyor.', 'Hayattan çıkarı olmayanların, ölümden de çıkarı olmayacaktır.', 'Zaten tehlikenin insanın en az beklediği yerden geldiğine inanırdı', 'Sabır bir ağaç gibidir, kökleri acı ama meyveleri çok tatlıdır.', 'Dünyanın en yoksul insanı, paradan başka hiçbir şeyi olmayandır.', 'Hayatının değeri uzun yaşanmasında değil, iyi yaşanmasındadır.', 'Üşüyorum, ama sen anılarla sarma beni ve anlat yalnızlığımızı', 'Gitmek fiilinin altını, çift çizgiyle en güzel trenler çizermiş.', 'İnsanların çoğunu ilgilendiren şeyler beni hiç ilgilendirmiyordu.', 'İnsanın kendi hayallerine para ödemesi umutsuzlukların en beteriydi', 'Bir klasiği her yeniden okuma, ilk okuma gibi bir keşif okumasıdır.', 'Neye tutunursan tutun eninde sonunda içeri çekilmekten kaçamıyordun', 'Sadece söylemek zorunda olduğum şeyleri dinleyecek birini istiyorum.', 'Kimi iyi tanıyorum dediysem sonrasında hep daha iyi tanımam gerekti.', 'Hem bir şey bilmez, hem de her şeye karışır, fikir beyân edersin.', 'Ben hasta bir adamım Gösterişsiz, içi hınçla dolu bir adamım ben', 'Kendi yaralarını iyileştirmezsen, herkesin bıçağı keskin kalır.', 'Gözler yalan söylemez derler, şimdi gözlerime yalan söyleteceğim.', 'Ruhun, bedeninden daha önce ölecektir. Artık hiçbir şeyden korkma.', 'Hayat senli de sensiz de devam edecek. Bunu ister kabul et, ister etme!', 'İnsan, can sıkıcı bir saç demetidir, ben de akılsız bir robotum.', 'Annen artık sallanan değil de, dünyayı sallayan biri olmuş desene.', 'Millet, bayram ve kandillerde tarihini, geçmiş ve geleceğini yaşar.', 'Şaşarım seven insan nasıl uyur? Aşıka her türlü uyku haramdır.', 'Bize benzer gayeler taşıyanlar en tehlikeli düşmanlarımız oluyor.', "Müona göre zaman, Dünya'daki bize göre daha yavaş akıyor olmalı.", '"Söylesene; beni kaybedecek kadar kimi, neyi kazanmak için gidiyordun?"', 'Savaşın keskin baltası kendilerini de yıkmıştı, umutlarını da.', 'Mutlu olmaya uğraşmaktan bir vazgeçsek çok iyi vakit geçireceğiz.', 'Ben tuttum birini sevdim, hayatı nasıl sevdiysem onu da öyle sevdim.', 'Bugün yaşadıkların, düne kadar ilmek ilmek dokudukların aslında.', 'Yazmak unutmaktır. Edebiyat dünyayı hiçe saymanın en uygun yoludur', 'Cinayet işlemek, ölenleri geri getirmez, sadece ölümü yüceltirdi.', 'Her şeyi hem olduğu gibi, hem de olması gerektiği gibi görmelisin.', "Ilk 'O'kulda sınıfta kaldım ben. Sonrası malum hâlâ 'O'kuldayım.", '"Erkek sevdiği zaman arzu yoktur; arzuladığı zaman ise, aşk yoktur."', 'Aşk, ölümsüz olmak istediğin bir savaş meydanı. Bir Cihan Kafes.', 'Boş bir adamın ne olduğunu düşünmek bile insana ürküntü verir.', 'Terapi, biri diğerinden daha dertli iki insanın karşılaşmasıdır.', 'Hayatın da kendini anlatmak için her zaman garip yöntemleri vardır.', 'İnsan aslında sahip olduklarının bilincinde olmayan bir kapitalist.', 'Bakın etrafa hep maziden şikayet ediyoruz, hepimiz onunla meşgulüz.', 'Shakespeare der ki: Soyulduğunda gülen, hırsızdan bir şey çalar.', 'Seni öldürmeyen şey, başladığı işi bitirmek için geri döner.', 'Görüntü onu görüyor, buna karşın o, görüntüyü görmüyordu.', 'Aşk, dört nala giden at gibidir, ne dizginden anlar, ne söz dinler.', 'Bazen insanın kaderi, başkalarının kaderi üzerinden yazılıyordu', 'Asıl acı çekilen acı değil sevilenin çektiği acıyı bilmektir.', 'Yüreklerin çarpmadığı yerlerde de yaprakların düşmesi gerekir.', 'Güzel nimetleri mahvetti insan, kader deyip şimdi geçti köşesine.', 'Öğrenmeye en fazla ihtiyaç duyduğunuz şeyi en iyi öğretirsiniz.', "Ağzımdan çıkanlar Tyler'ın sözleri. Melek gibi bir adamdım ben.", 'Olay şu: günün sonunda aynada hala kendi yüzüne bakman gerekiyor.', 'Kendine gel Osmancık, biz intikam peşinde değil, devlet peşindeyiz', 'Tarihin öyle bir devrindeyiz ki iktisadi dava belki en sonda geliyor.', 'Hayat kendinizi bulmaya dair değildir. Daha çok çikolataya dairdir.', 'Hayvan hakları daha büyük kafesler değil boş kafesler talep eder.', 'Aklın varsa bir başka akılla dost ol da, işlerini danışarak yap.', 'Ben cılız bir suymuşum da sen başına buyruk akmayı severmişsin.', 'Dostlarından kuşkulanmak, başa geçenlere özgü bir hastalıktır.', 'Yalnızlığa dayanabilen insan yeryüzünün en kuvvetli insanıdır.', 'Aslına bakılırsa kim kaderini elinde tutabiliyor ki tam anlamıyla?', 'Geldiğimiz ülkelerin felaketi hiç bir umutlarının olmayışında.', 'Bu şehirde öyle yerler var ki, benim için adeta yasaklı bölgeler.', 'Kelimeler olmadan yaşadıkları için mi hayvanlar daha az korkuyor ?', 'Arabamıza vücudumuz gibi davransaydık, bir yılda hurdaya dönerdi.', 'Dağınık masa, dağınık kafaya işaretse, boş masa neye işaret ?', 'Bir devleti kurmak için bin yıl ister, yıkmak için bir saat yeter.', 'Eğer sonsuzluk bitimsizse, her şeyin sonu bile onu yıkamayacaktır.', 'Ne istedigini kendin bilmiyor musun? Nasıl dayanabiliyorsun bilmemeye?', 'İlk aşkımızı asla unutmayız. Benimkinin sonu öldürülmek oldu.', 'Gölde daire şeklinde yayılan her dalga er geç etkisini kaybederdi.', 'İnsan olabilmek için erkek olmanın yeteceğini sanıp aldanmıştı.', 'Amaç aşk uğruna ölmek değil, uğruna ölünecek aşkı bulmaktır.', 'Demek insanlar alçalınca, vahşi hayvandan daha tehlikeli olabiliyor.', 'İnsanın sevdiği bir ev olunca, kendisine mahsus bir hayatı da olur.', 'Bize bir kaç deli gerek, şu akıllıların yol açtığı duruma bak.', 'Kusursuz bir insan ararsan, dört dörtlük bir yalnızlık yaşarsın.', 'Fakat herkes bilir ki hayat, yaşanmak zahmetine değmeyen bir şeydir.', 'Sadece sevgi ve iyiliği anlatın, diğerlerini herkes söylüyor zaten', 'İmkansız şeyler kafamızın içinde olur. Çünkü hayat gerçektir.', 'Şiir yazmanın insanı uçurumun kenarına sürükleyen bir yanı var.', 'İnsanoğlu daima haddini aşma eğilimindedir, zaten hatası da budur.', 'Sahibine yetişecek hecelerin yoksa, vurursun sükutunu kör bir geceye', 'Varlığınızda kıymetinizi bilmeyenleri, yokluğunuzla terbiye edin.', 'Her toplum, kadına verdiği değere oranla gelişir ya da ilkelleşir.', 'Gerçek dost çınar ağacı gibidir, meyvesi olmasa da gölgesi yeter.', 'Bir düşü gerçekleştirme olasılığı yaşamı ilginçleştiriyor.', 'Herkes bir şeyler bekler, ama bir ananın beklediği okşanmaktır hep', 'Uygarlıklar, en yukarıdaki en aşağıdakini unuttuğunda çöküyor.', 'Ortalıkta horultudan geçilmiyordu. İçleri rahat uyumayanlar horlar.', "Yalnız olduğunu en çok,'yalnız değilsin' dediklerinde hissedersin.", 'Ben senin için her mevsim olurdum da, sen dünyam olmayı beceremedin.', 'Senin herkesten beklediğin muamele, herkesin de beklediği muameledir.', 'Ne yazık ki aşk hayalin çocuğu, hayal kırıklığının annesidir.'
]


@client.on(events.NewMessage(pattern="^/soztag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir. 🐙**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Etikete Başlamak için sebep yazın... 🐙\n\n(Örnek: /soztag Herkese Merhaba!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı. 🐙**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{msg}**\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n🐙 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")


gisim = ['Üzümlü kek ✨', 'Nar çiçeği ✨', 'Papatya 🌼', 'Karanfil ✨', 'Gül 🌹', 'Ayıcık 🐻', 'Mutlu panda 🐼', 'Ay pare 🌛', 'Ballı lokma ✨', 'Lale 🌷', 'Ahtapot 🐙', 'Zambak ⚜', 'Akasya 🌿', 'Akşam Sefası 🌛', 'Begonvil 🥀', 'Begonya 🪴', 'Bambu 🎍', 'Fesleğen 🌿', 'Kasımpatı 🌸', 'Manolya 🌾', 'Boncuk 🧿', 'Badem 🥭', 'Minnoş 🐹', 'Ponçik 🐣', 'Pofuduk 🐼', 'Unicorn 🦄', 'Karamel 🍫', 'Fındık 🌰', 'Fıstık 🥜', 'Pamuk ☁️', 'Minnoş 🥰', 'Zeytin 🫒', 'Afrodit 🧚🏻', 'Nergis ✨', 'Sümbül ☘️', 'Nilüfer ☘️', 'Menekşe ⚜️', 'Lavanta ✨', 'Gül pare 🌺', 'Reyhan 🌷', 'Kaktüs 🌵', 'Buket 💐', 'Başak 🌾', 'Kar Tanesi ❄️', 'Tospik 🐢', 'Kelebek 🦋', 'Tavşan 🐰', 'Şeker 🍬', 'Böğürtlen ☘️', 'Orkide ☘️', 'Manolya ✨', 'Ayçiçeği 🌻', 'Tweety 🐥', 'Star ✨', 'Yonca 🍀', 'Ateş böceği ✨']


@client.on(events.NewMessage(pattern="^/isimtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir. 🐙**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Etikete Başlamak için sebep yazın... 🐙\n\n(Örnek: /isimtag Herkese Merhaba!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı. 🐙**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(gisim)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"**{msg}**\n**{usrtxt}**")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n🐙 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(gisim)}](tg://user?id={usr.id})"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")


futbol = ['Maldonado', 'Lionel Messi', 'Bobô', 'Matías Delgado', 'Márcio Nobre1', 'Rodrigo Tello', 'Federico Higuaín', 'Lamine Diatta', 'Édouard Cissé', 'Gordon Schildenfeld', 'Filip Hološko', 'Anthony Šerić', 'Tomáš Sivok', 'Tomáš Zápotočný', 'Fabian Ernst', 'Michael Fink', 'Matteo Ferrari', 'Rodrigo Tabata', 'Ricardo Quaresma', 'Roberto Hilbert', 'Guti', 'Marco Aurélio1', 'Manuel Fernandes', 'Simao Sabrosa', 'Hugo Almeida', 'Sidnei', 'Bébé', 'Júlio Alves', 'Edú', 'Julien Escudé', 'Allan McGregor', 'Dentinho', 'Mamadou Niang', 'Pedro Franco', 'Michael Eneramo', 'Atiba Hutchinson', 'Ramon Motta', 'Jermaine Jones', 'Dany Nounkeu', 'Demba Ba', 'José Sosa', 'Alexander Milošević', 'Daniel Opare', 'Duško Tošić', 'Andreas Beck', 'Luiz Rhodolfo', 'Mario Gómez', 'Denis Boyko', 'Aras Özbiliz', 'Alexis Delgado', 'Marcelo Guedes', 'Fabri', 'Adriano Correia', 'Talisca', 'Vincent Aboubakar', 'Ryan Babel', 'Matej Mitrović', 'Pepe', 'Álvaro Negredo', 'Jeremain Lens', 'Gary Medel', 'Cyle Larin', 'Vágner Love', 'Domagoj Vida', 'Enzo Roco', 'Loris Karius', 'Adem Ljajić', 'Nicolas Isimat-Mirin', 'Shinji Kagawa', 'Tyler Boyd', 'Douglas', 'Víctor Ruiz', 'Pedro Rebocho', "Georges-Kévin N'Koudou", 'Muhammed Elneni', 'Abdoulay Diaby', 'Ajdin Hasić', 'Kevin-Prince Boateng', "Fabrice N'Sakala", 'Bernard Mensah', 'Welinton', 'Francisco Montero', 'Josef de Souza', 'Valentin Rosier', 'Raşit Gezzal', 'Alex Teixeira', 'Michy Batshuayi', 'Miralem Pjanić', 'Gedson Fernandes', 'Romain Saïss', 'Mert Günok', 'Ersin Destanoğlu', 'Emre Bilgin', 'Goktug Baytekin', 'Domagoj Vida', 'Welinton', 'Douglas', 'Fabrice NSkala', 'Umut Meras', 'Francisco Montero', 'Valentin Rosier', 'Kerem Kalafat', 'Rıdvan Yılmaz', 'Serdar Saatçi', 'Serkan Emrecan Terzi', 'Aytug Batur Komec', 'Atiba Hutchinson', 'Mehmet Topal', 'Miralem Pjanic', 'Adem Ljajic', 'Alex Teixeira', 'Necip Uysal', 'Gökhan Töre', 'Rachid Ghezzal', 'Oğuzhan Özyakup', 'Georges-Kevin Nkoudou', 'Muhayer Oktay', 'Can Bozdogan', 'Berkay Vardar', 'Emirhan İlkhan', 'Emirhan Delibas', 'Demir Tiknaz', 'Jeremain Lens', 'Michy Batshuayi', 'Kenan Karaman', 'Cyle Larin', 'Güven Yalçın', 'Koray Yagci', 'Ariel Ortega', 'Robert Enke', 'Vladimir Beschastnykh', 'Ivaylo Petkov', 'Sergiy Rebrov', 'Stjepan Tomas', 'Pierre van Hooijdonk', 'Marco Aurelio', 'Fábio Luciano', 'Mert Nobre', 'Fabiano', 'Alex De Souza', 'Stephen Appiah', 'Nicolas Anelka', 'Mateja Kežman', 'Edu Dracena', 'Diego Lugano', 'Deivid', 'Roberto Carlos', 'Wederson', 'Claudio Maldonado', 'Josico', 'Daniel Güiza', 'Fábio Bilica', 'André Santos', 'Cristian Baroni', 'Miroslav Stoch', 'Issiar Dia', 'Mamadou Niang', 'Joseph Yobo', 'Emmanuel Emenike', 'Reto Ziegler', 'Henri Bienvenu', 'Moussa Sow', 'Dirk Kuyt', 'Miloš Krasić', 'Raul Meireles', 'Pierre Webó', 'Bruno Alves', 'Michal Kadlec', 'Samuel Holmén', 'Diego', 'Simon Kjær', 'Fernandão', 'Abdoulaye Ba', 'Fabiano Ribeiro', 'Nani', 'Josef de Souza', 'Robin van Persie', 'Lazar Marković', 'Aatif Chahechouhe', 'Gregory van der Wiel', 'Roman Neustädter', 'Martin Škrtel', 'Jeremain Lens', 'Oleksandr Karavayev', 'Mathieu Valbuena', 'Nebil Dirar', 'Carlos Kameni', 'Mauricio Isla', 'Elif Elmas', 'Roberto Soldado', 'Giuliano', 'Luís Neto', 'Vincent Janssen', 'André Ayew', 'Islam Slimani', 'Michael Frey', 'Diego Reyes', 'Jailson', 'Yassine Benzia', 'Victor Moses', 'Miha Zajc', 'Max Kruse', 'Allahyar Seyyadmeneş', 'Vedat Muriqi', 'Garry Rodrigues', 'Zanka', 'Adil Rami', 'Luiz Gustavo', 'Simon Falette', 'Filip Novák', 'Mame Thiam', 'José Sosa', 'Mauricio Lemos', 'Enner Valencia', 'Marcel Tisserand', 'Mbwana Samatta', 'Papiss Cissé', 'Kemal Ademi', 'Dimitris Pelkas', 'Diego Perotti', 'Attila Szalai', 'Bright Osayi-Samuel', 'Mesut Özil', 'Steven Caulker', 'Kim Min-jae', 'Diego Rossi', 'Mërgim Berisha', 'Max Meyer', 'Miguel Crespo', 'Erol Bulut', 'Saffet Akbaş', 'Tayfun Korkut', 'Elvir Bolić', 'Mustafa Doğan', 'Samuel Johnson', 'Abdullah Ercan', 'Ogün Temizkanoğlu', 'Semih Şentürk', 'Ali Güneş', 'Serhat Akın', 'Ümit Özat', 'Volkan Demirel', 'Tuncay Şanlı', 'Selçuk Şahin', 'Fabio Luciano', 'Mehmet Yozgatlı', 'Mehmet Aurelio', 'Serkan Balcı', 'Önder Turacı', 'Uğur Boral', 'Gökhan Gönül', 'Gökçek Vederson', 'Colin Kâzım Richards', 'Emre Belözoğlu', 'Mehmet Topuz', 'Bekir İrtegün', 'Caner Erkin', 'Hasan Ali Kaldırım', 'Mehmet Topal', 'Alper Potuk', 'Şener Özbayraklı', 'Ozan Tufan', 'Aykut Erçetin', 'Çağlar Birinci', 'Gökhan Zan', 'Ceyhun Gülselam', 'Aydın Yılmaz', 'Selçuk İnan', 'Johan Elmander', 'Felipe Melo', 'Dida', 'Cafu', 'Stam', 'Nesta', 'Maldini', 'Pirlo', 'Gattuso', 'Seedorf', 'Kaka', 'Shevchenko', 'Inzaghi', 'Crespo', 'Diego Altube', 'Thibaut Courtois', 'Alphonse Areola', 'Andriy Lunin', 'Lucas Canizares', 'Luis Lopez', 'Toni Fuidias', 'Diego Del Alamo', 'Luis Federico', 'Sergio Ramos', 'Raphael Varane', 'Daniel Carvajal', 'Adrian De La Fuente', 'Ferland Mendy', 'Marcelo', 'Eder Militao', 'Alvaro Odriozola', 'Victor Chust', 'Sergio Santos', 'Pablo Ramon Parra', 'Miguel Gutierrez', 'David Alaba', 'Jesus Vallejo', 'Rafa Marin', 'Mario Gila', 'Reinier', 'Marco Asensio', 'Federico Valverde', 'Brahim Diaz', 'Luka Modric', 'Toni Kroos', 'Isco', 'Carlos Casemiro', 'Lucas Vazquez', 'Martin Odegaard', 'Marvin Park', 'Sergio Arribas', 'Antonio Blanco', 'Hugo Duro', 'Eduardo Camavinga', 'Dani Ceballos', 'Peter Gonzalez', 'Karim Benzema', 'Luka Jovic', 'Eden Hazard', 'Gareth Bale', 'Vinicius Junior', 'Rodrygo', 'James Rodriguez', 'Mariano Diaz', 'Borja Mayoral', 'Oscar Aranda', 'Juan Latasa', 'Neto', 'Marc-Andre Ter Stegen', 'Inaki Pena', 'Arnau Tenas', 'Lazar Carevic', 'Jordi Alba', 'Sergi Roberto', 'Ronald Araujo', 'Samuel Umtiti', 'Nelson Semedo', 'Clement Lenglet', 'Dani Morer', 'Junior Firpo', 'Gerard Pique', 'Sergio Akieme', 'Santiago Ramos', 'Arnau Comas', 'Sergino Dest', 'Oscar Mingueza', 'Eric Garcia', 'Emerson', 'Alejandro Balde', 'Dani Alves', 'Mika Marmol', 'Sergio Busquets', 'Hiroki Abe', 'Alex Collado', 'Frenkie De Jong', 'Ivan Rakitic', 'Arturo Vidal', 'Riqui Puig', 'Guillem Jaime', 'Miralem Pjanic', 'Philippe Coutinho', 'Carles Alena', 'Konrad De La Fuente', 'Ilaix Moriba', 'Matheus Fernandes', 'Yusuf Demir', 'Nico Gonzalez', 'Abde Ezzalzouli', 'Alvaro Sanz', 'Ferran Jutgla', 'Matheus Pereira', 'Lucas De Vega', 'Estanis Pedrola', 'Adama Traore', 'Luis Suarez', 'Ousmane Dembele', 'Antoine Griezmann', 'Ansu Fati', 'Lionel Messi', 'Rey Manaj', 'Martin Braithwaite', 'Memphis Depay', 'Sergio Agüero', 'Luuk De Jong', 'Ilias Akhomach', 'Ferran Torres', 'Pierre Aubameyang', 'Albert Riera', 'Milan Baroš', 'Tomáš Ujfaluši', 'Mehmet Batdal', 'Serkan Kurtuluş', 'Yiğit Gökoğlan', 'Hakan Balta', 'Fernando Muslera', 'Semih Kaya', 'Emmanuel Eboué', 'Yekta Kurtuluş', 'Engin Baytar', 'Emre Çolak', 'Sabri Sarıoğlu', 'Servet Çetin', 'Necati Ateş', 'Ufuk Ceylan', 'Sercan Yıldırım', 'Fernando Muslera', 'Felipe Melo', 'Hamit Altıntop', 'Gökhan Zan', 'Blerim Džemaili', 'Aydın Yılmaz', 'Selçuk İnan', 'Umut Bulut', 'Wesley Sneijder', 'Bruma', 'Alex Telles', 'Burak Yılmaz', 'Sinan Gümüş', 'Goran Pandev', 'Aurélien Chedjou', 'Fernando Muslera', 'Mariano', 'Maicon', 'Serdar Aziz', 'Ahmet Çalık', 'Tolga Ciğerci', 'Yasin Öztekin', 'Selçuk İnan', 'Eren Derdiyok', 'Younès Belhanda', 'Sinan Gümüş', 'Martin Linnes', 'Ryan Donk', 'Cédric Carrasso', 'Şener Özbayraklı', 'Omar Elabdellaoui', 'Taylan Antalyalı', 'Henry Onyekuru', 'Ryan Babel', 'Radamel Falcao', 'Halil Dervişoğlu', 'Oghenekaro Etebo', 'Martin Linnes', 'Ryan Donk', 'Oğulcan Çağlayan', 'Kerem Aktürkoğlu', 'Ömer Bayram', 'Emre Akbaba', 'Cristiano Ronaldo', 'Pele', 'Maradona', 'Ronaldo', 'Thierry Henry', 'Kaka', 'Sergio Agüero', 'Xavi', 'Ruud Gullit', 'Arthur Zico', 'Lev Yashin', 'Iniesta', 'Lothar Matthäus', 'Giuseppe Meazza', 'Franz Beckenbauer', 'George Best', 'Roberto Baggio', 'Johan Cruyff', 'Luis Figo', 'Andrea Pirlo', 'Marco Van Basten', 'Zlatan Ibrahimovic', 'Sandro Mazzola', 'Ferenc Puskas', 'Zinedine Zidane', 'Alfredo Di Stéfano', 'Rio Ferdinand', 'Paolo Maldini', 'Robin van Persie', 'Iker Casillas', 'Neymar', 'Fabio Cannavaro', 'Yaya Toure', 'Edinson Cavani', 'Gabriel Batistuta', 'Thiago Silva', 'Dennis Bergkamp', 'Franck Ribery', 'Carles Puyol', 'Mesut Özil', 'Dani Alves', 'David Silva', 'Karim Benzema', 'Javier Zanetti', 'Radamel Falcao', 'Bastian Schweinsteiger', 'Gianluigi Buffon', 'Arjen Robben', 'Wayne Rooney', 'Luis Suarez', 'Mbappe', 'Juan Román Riquelme', 'Sergio Ramos', 'Muhammed Salah', 'Cesc Fabregas', 'Gerard Pique', 'Pepe', 'Didier Drogba', 'Robert Lewandowski', 'David Villa', 'Wesley Sneijder', 'Philipp Lahm', "Samuel Eto'o", 'Carlos Tevez', 'Sergio Busquets', 'Samir Nasri', 'Eden Hazard', 'Diego Forlan', 'Klaas Jan Huntelaar', 'Sabri Sarıoğlu']


@client.on(events.NewMessage(pattern="^/futbol ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir. 🐙**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Etikete Başlamak için sebep yazın... 🐙\n\n(Örnek: /futbol Herkese Merhaba!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı. 🐙**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(futbol)}](tg://user?id={usr.id}) , "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"**{msg}**\n**{usrtxt}**")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n🐙 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(futbol)}](tg://user?id={usr.id})"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")


@client.on(events.NewMessage(pattern='^/stats ?(.*)'))
async def son_durum(event):
    global anlik_calisan,grup_sayi,ozel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
      return
    await event.respond(f"**OCTO Tagger İstatistikleri 🤖**\n\nToplam Grup: `{len(grup_sayi)}`\nAnlık Çalışan Grup: `{len(anlik_calisan)}`")


@client.on(events.NewMessage(pattern="^/octotag ?(.*)"))
async def mentionall(event):
  global anlik_calisan,ozel_list
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in ozel_list:
    return await event.respond("**Bu komutu sadece bot yöneticileri kullanabilir. 🐙**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Etikete Başlamak için sebep yazın... 🐙**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı.**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id}) , **"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"**{msg}**\n{usrtxt}")
        await asyncio.sleep(1.5)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n🐙 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id}) , **"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(1.5)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")



emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir. 🐙**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Etikete Başlamak için sebep yazın... 🐙\n\n(Örnek: /etag Herkese Merhaba!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı. 🐙**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"**{msg}**\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n🐙 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"\n🐙 - [{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")



@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir. 🐙**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Etikete Başlamak için sebep yazın... 🐙\n\n(Örnek: /tag Herkese Merhaba!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı. 🐙**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id}) , **"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"**{msg}**\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n🐙 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id}) , **"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir. 🐙**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Etikete Başlamak için sebep yazın... 🐙\n\n(Örnek: /tektag Bugün Nasılsın?)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı. 🐙**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id}) **"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{msg}**\n**{usrtxt}**")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n🐙 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id}) **"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	

kurucu_id = 910247612

admins = [kurucu_id, 1900050206, 996686235, 1807248089, 1705269676, 5192739364, 5232252671, 5268166904, 5081793989, 1191088523]
# 5081793989 = mantuvar 1191088523 = Lim 5268166904 = hatice


@client.on(events.NewMessage(pattern='^(?i)reset'))
async def reset(event):
  if not event.is_private:
    await event.respond("Bu komut sadece özelden yazılabilir")
    return

  if event.sender_id in admins:
    await event.respond("Reset vakti!")

    sender = await event.get_sender()

    entity = await client.get_entity(-1001670915989)
    await client.send_message(entity=entity,message=f'🔨 <a href="tg://user?id={event.sender_id}">{sender.username}</a> ({event.sender_id}) bota reset atıyor...', parse_mode='html')

    os.system('sudo bash /etc/rc.local')
  else:
    await event.respond("Yetkin yok!!")
    return



@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komutu sadece grup veya kanallarda kullanabilirsin.**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir. 🐙**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Etikete Başlamak için sebep yazın... 🐙\n\n(Örnek: /atag Herkese Merhaba!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı. 🐙**")
  
    async for usr in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id}) , **"
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiket İşlemi Bitti. 🐙")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"**{msg}**\n\n**{usrtxt}**")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id}) , **"
      if event.chat_id not in anlik_calisan:
        await event.respond("**✅ Etiket işlemi durduruldu.**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""

    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")



print(">> Bot çalıyor merak etme 🚀 @OctopusGameSahip  bilgi alabilirsin <<")
client.run_until_disconnected()

# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8154426339")
APP_ID = int(os.environ.get("APP_ID", "")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002170811388")) #Your db channel Id
OWNER = os.environ.get("OWNER", "sewxiy") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "73029001")) # Owner id
admin_ids = [OWNER_ID]  # OWNER_ID sudah didefinisikan di file config.py
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluooo")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "30"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/Zerozerozoro")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>❏ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ\nsɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/Zerozerozoro>Pecel Lele</a></blockquote></b>"
#ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/cosmic_freak>Yato</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/otakuflix_network>ᴏᴛᴀᴋᴜғʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/anime_cruise_netflix>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>\n◈ sᴇʀɪᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/webseries_flix>ᴡᴇʙsᴇʀɪᴇs ғʟɪx</a>\n◈ ᴀᴅᴜʟᴛ ᴍᴀɴʜᴡᴀ : <a href=https://t.me/pornhwa_flix>ᴘᴏʀɴʜᴡᴀs</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/cosmic_freak>subaru</a></blockquote></b>"
#ABOUT_TXT = "<b><blockquote expandable>ᴛʜɪs ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ \n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/cosmic_fk>Bokep</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>❏ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ\nsɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/Zerozerozoro>Pecel Lele</a></blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\n<blockquote> ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

CMD_TXT = """
<blockquote><b>❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs</b></blockquote>
<b>├ /start :</b> ᴍᴜʟᴀɪ ʙᴏᴛ ᴀᴛᴀᴜ ᴅᴀᴘᴀᴛᴋᴀɴ ᴘᴏsᴛɪɴɢᴀɴ
<b>├ /batch : </b>ʙᴜᴀᴛ ᴛᴀᴜᴛᴀɴ ᴜɴᴛᴜᴋ ʟᴇʙɪʜ ᴅᴀʀɪ sᴀᴛᴜ ᴘᴏsᴛɪɴɢᴀɴ
<b>├ /genlink : </b>ʙᴜᴀᴛ ᴛᴀᴜᴛᴀɴ ᴜɴᴛᴜᴋ sᴀᴛᴜ ᴘᴏsᴛɪɴɢᴀɴ
<b>├ /users :</b> ʟɪʜᴀᴛ sᴛᴀᴛɪsᴛɪᴋ ʙᴏᴛ
<b>├ /broadcast :</b> ᴋɪʀɪᴍ ᴘᴇsᴀɴ sɪᴀʀᴀɴ ᴋᴇ ᴘᴇɴɢɢᴜɴᴀ ʙᴏᴛ
<b>├ /dbroadcast : </b>ᴋɪʀɪᴍ ᴘᴇsᴀɴ sɪᴀʀᴀɴ ᴅᴇɴɢᴀɴ ᴘᴇɴɢʜᴀᴘᴜsᴀɴ ᴏᴛᴏᴍᴀᴛɪs
<b>├ /stats : </b>ᴘᴇʀɪᴋsᴀ ᴡᴀᴋᴛᴜ ᴀᴋᴛɪғ ʙᴏᴛ
<b>├ /custom_batch : </b>ʙᴜᴀᴛ ʙᴀᴛᴄʜ ᴋᴜsᴛᴏᴍ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ/ɢʀᴜᴘ
<b>├ /dlt_time : </b>ᴀᴛᴜʀ ᴡᴀᴋᴛᴜ ᴘᴇɴɢʜᴀᴘᴜsᴀɴ ᴏᴛᴏᴍᴀᴛɪs ᴜɴᴛᴜᴋ ғɪʟᴇ
<b>├ /check_dlt_time : </b>ᴘᴇʀɪᴋsᴀ ᴘᴇɴɢᴀᴛᴜʀᴀɴ ᴡᴀᴋᴛᴜ ᴘᴇɴɢʜᴀᴘᴜsᴀɴ sᴀᴀᴛ ɪɴɪ
<b>├ /ban : </b>ʟᴀʀᴀɴɢ ᴘᴇɴɢɢᴜɴᴀ ᴅᴀʀɪ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ
<b>├ /unban : </b>ʙᴀᴛᴀʟᴋᴀɴ ʟᴀʀᴀɴɢᴀɴ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ sᴇʙᴇʟᴜᴍɴʏᴀ ᴅɪʟᴀʀᴀɴɢ
<b>├ /banlist : </b>ᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀғᴛᴀʀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪʟᴀʀᴀɴɢ
<b>├ /addchnl :</b> ᴛᴀᴍʙᴀʜᴋᴀɴ ᴄʜᴀɴɴᴇʟ ᴜɴᴛᴜᴋ ʟᴀɴɢɢᴀɴᴀɴ ᴘᴀᴋsᴀ
<b>├ /delchnl : </b>ʜᴀᴘᴜs ᴄʜᴀɴɴᴇʟ ʟᴀɴɢɢᴀɴᴀɴ ᴘᴀᴋsᴀ
<b>├ /listchnl :</b> ʟɪʜᴀᴛ sᴇᴍᴜᴀ ᴄʜᴀɴɴᴇʟ ʟᴀɴɢɢᴀɴᴀɴ ᴘᴀᴋsᴀ ʏᴀɴɢ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ
<b>├ /fsub_mode : </b>ᴀᴋᴛɪғᴋᴀɴ ᴀᴛᴀᴜ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ ʟᴀɴɢɢᴀɴᴀɴ ᴘᴀᴋsᴀ
<b>├ /pbroadcast :</b> sᴇᴍᴀᴛᴋᴀɴ sɪᴀʀᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴏʙʀᴏʟᴀɴ ᴘᴇɴɢɢᴜɴᴀ
<b>├ /add_admin : </b>ᴛᴀᴍʙᴀʜᴋᴀɴ ᴀᴅᴍɪɴ ʙᴀʀᴜ
<b>├ /deladmin : </b>ʜᴀᴘᴜs ᴀᴅᴍɪɴ
<b>├ /admins :</b> ᴅᴀғᴛᴀʀ sᴇᴍᴜᴀ ᴀᴅᴍɪɴ sᴀᴀᴛ ɪɴɪ

<blockquote> Animax! </blockquote>
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @nova_flix</b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False") == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"
#--------------------------------------------


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

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

import asyncio
import os
import random
import sys
import time
import speedtest
from datetime import datetime, timedelta
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode, ChatAction
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, ChatInviteLink, ChatPrivileges
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserNotParticipant
from bot import Bot
from config import *
from helper_func import *
from database.database import *

start_time = time.time()

def format_uptime(uptime):
    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if days > 0:
        return f"{days}d {hours}h {minutes}m {seconds}s"
    elif hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"

@Bot.on_message(filters.command('ping'))
async def ping_command(client: Bot, message: Message):
    start_time = time.time()
    msg = await message.reply("⌛️")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = timedelta(seconds=time.time() - start_time_bot)
    uptime_str = format_uptime(uptime)
    await msg.edit_text(f"💡 Ping: `{ping_time} ms`\n🕒 Uptime: `{uptime_str}`")
    
@Bot.on_message(filters.command(["speedtest", "stats"]) & admin)
async def stats(client, message):
    msg = await message.reply_text("Getting stats...")
    start_time_msg = time.time()
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        test.download()
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await msg.edit_text(e)
        return
    ping_time = round((time.time() - start_time_msg) * 1000, 3)
    uptime = timedelta(seconds=time.time() - start_time)
    uptime_str = format_uptime(uptime)
    output = f"""
<b>📊 Stats Bot</b>
<blockquote>⏰ Uptime: {uptime_str}</blockquote>
<b>📈 Speedtest Results</b>
<blockquote>👥 <b>Client :</b>
    ⟡ ISP: {result['client']['isp']}
    ⟡ Country: {result['client']['country']}
🏢 <b>Server :</b>
    ⟡ Name: {result['server']['name']}
    ⟡ Country: {result['server']['country']}, {result['server']['cc']}
    ⟡ Sponsor: {result['server']['sponsor']}
    ⟡ Ping: {result['ping']}
    ⟡ Download: {round(result['download'] / 1024 / 1024, 2)} Mbps
    ⟡ Upload: {round(result['upload'] / 1024 / 1024, 2)} Mbps</blockquote>
"""
    await msg.edit_text(output)


@Bot.on_message(filters.command('id'))
async def get_info(client: Bot, message: Message):
    try:
        if message.chat.type in ["group", "supergroup"]:
            await message.reply(f"**ID Grup:** `{message.chat.id}`")
        elif message.chat.type == "channel":
            await message.reply(f"**ID Channel:** `{message.chat.id}`")
        elif message.chat.type == "private":
            await message.reply(f"**ID User:** `{message.from_user.id}`")
    except Exception as e:
        await message.reply(f"Error: {e}")


@Bot.on_message(filters.command('p'))
async def get_info(client: Bot, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        chat = await client.get_chat(message.chat.id)
        members_count = await client.get_chat_members_count(chat.id)
        chat_member = await client.get_chat_member(chat.id, message.from_user.id)
        await message.reply(f"**Info Grup**\n\n"
                            f"**ID:** `{chat.id}`\n"
                            f"**Judul:** `{chat.title}`\n"
                            f"**Deskripsi:** `{chat.description}`\n"
                            f"**Jumlah Anggota:** `{members_count}`\n"
                            f"**Status Anda:** `{chat_member.status}`\n"
                            f"**Izin Anda:** `{chat_member.permissions}`")
    elif message.chat.type == "channel":
        chat = await client.get_chat(message.chat.id)
        members_count = await client.get_chat_members_count(chat.id)
        await message.reply(f"**Info Channel**\n\n"
                            f"**ID:** `{chat.id}`\n"
                            f"**Judul:** `{chat.title}`\n"
                            f"**Deskripsi:** `{chat.description}`\n"
                            f"**Jumlah Anggota:** `{members_count}`")
    elif message.chat.type == "private":
        user = await client.get_users(message.from_user.id)
        await message.reply(f"**Info User**\n\n"
                            f"**ID:** `{user.id}`\n"
                            f"**Nama:** `{user.first_name}`\n"
                            f"**Username:** `{user.username}`\n"
                            f"**Status Online:** `{user.status}`")
#=====================================================================================##

WAIT_MSG = "<b>Loading....</b>"

#=====================================================================================##


@Bot.on_message(filters.command('users') & filters.private & admin)
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await db.full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

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

#=====================================================================================##

#AUTO-DELETE

@Bot.on_message(filters.private & filters.command('dlt_time') & admin)
async def set_delete_time(client: Bot, message: Message):
    try:
        duration = int(message.command[1])

        await db.set_del_timer(duration)

        await message.reply(f"<b>Dᴇʟᴇᴛᴇ Tɪᴍᴇʀ ʜᴀs ʙᴇᴇɴ sᴇᴛ ᴛᴏ <blockquote>{duration} sᴇᴄᴏɴᴅs.</blockquote></b>")

    except (IndexError, ValueError):
        await message.reply("<b>Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ᴅᴜʀᴀᴛɪᴏɴ ɪɴ sᴇᴄᴏɴᴅs.</b> Usage: /dlt_time {duration}")

@Bot.on_message(filters.private & filters.command('check_dlt_time') & admin)
async def check_delete_time(client: Bot, message: Message):
    duration = await db.get_del_timer()

    await message.reply(f"<b><blockquote>Cᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇʀ ɪs sᴇᴛ ᴛᴏ {duration}sᴇᴄᴏɴᴅs.</blockquote></b>")

#=====================================================================================##

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

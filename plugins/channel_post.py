#(©)Codexbotz
import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from bot import Bot
from helper_func import encode, admin

DOWNLOAD_CHANNEL_ID = -1002573263047  # ganti dengan ID channel download

@Bot.on_message(filters.private & admin & ~filters.command(['start', 'commands','users','broadcast','batch', 'custom_batch', 'genlink','stats', 'dlt_time', 'check_dlt_time', 'dbroadcast', 'ban', 'unban', 'banlist', 'addchnl', 'delchnl', 'listchnl', 'fsub_mode', 'pbroadcast', 'add_admin', 'deladmin', 'admins']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Tunggu", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return

    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("📥 Save File", url=f'{link}')]])

    try:
        download_message = await message.copy(chat_id = DOWNLOAD_CHANNEL_ID, caption = f"ini caption contoh\n\n{link}", reply_markup=reply_markup, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        download_message = await message.copy(chat_id = DOWNLOAD_CHANNEL_ID, caption = f"ini caption contoh\n\n{link}", reply_markup=reply_markup, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return

    await reply_text.edit(f"<b>Here is your link</b>\n\n{link}", reply_markup=reply_markup, disable_web_page_preview = True)

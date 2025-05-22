from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

def register_handlers(app):
    # Menu Setting
    @app.on_message(filters.command(["setting"]))
    async def setting_menu(client, message: Message):
        keyboard = [
            [InlineKeyboardButton("Daftar Admin", callback_data="daftar_admin")],
            [InlineKeyboardButton("Set Welcome", callback_data="set_welcome")],
            [InlineKeyboardButton("Set Force Message", callback_data="set_force_msg")],
            [InlineKeyboardButton("Tutup", callback_data="close")],
        ]
        await message.reply_text(
            "Menu Setting",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # Callback untuk Daftar Admin
    @app.on_callback_query(filters.regex("daftar_admin"))
    async def daftar_admin(client, callback_query: CallbackQuery):
        await callback_query.message.edit_text("Fitur Daftar Admin")
        await callback_query.answer("Daftar Admin")

    # Callback untuk Set Welcome
    @app.on_callback_query(filters.regex("set_welcome"))
    async def set_welcome(client, callback_query: CallbackQuery):
        await callback_query.message.edit_text("Fitur Set Welcome")
        await callback_query.answer("Set Welcome")

    # Callback untuk Set Force Message
    @app.on_callback_query(filters.regex("set_force_msg"))
    async def set_force_msg(client, callback_query: CallbackQuery):
        await callback_query.message.edit_text("Fitur Set Force Message")
        await callback_query.answer("Set Force Message")

    # Callback untuk Tutup
    @app.on_callback_query(filters.regex("close"))
    async def close(client, callback_query: CallbackQuery):
        await callback_query.message.delete()
        await callback_query.answer("Menu Ditutup")

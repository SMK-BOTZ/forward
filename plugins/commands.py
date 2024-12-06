from plugins.forcesub import ForceSub
import os
import sys
import pytz
import asyncio 
from database import db, mongodb_version
from config import Config, temp
from platform import python_version
from translation import Translation
from datetime import datetime
from pyrogram import Client, filters, enums, __version__ as pyrogram_version
from pyrogram.types import *
TIMEZONE = "Asia/Kolkata"

main_buttons = [[
        InlineKeyboardButton('❗️ ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton('📜 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/vr_unreal'),
        InlineKeyboardButton('📣 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/vr_support')
        ],[
        InlineKeyboardButton('💳 ᴅᴏɴᴀᴛᴇ', callback_data='donate')
        ]]
#===================Start Function===================#

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    user = message.from_user
        
    # Check for force subscription
    Fsub = await ForceSub(client, message)
    if Fsub == 400:
        return
            
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, message.from_user.mention)
        # Log the new user to the log channel
        log_channel = Config.LOG_CHANNEL  # Replace with your log channel ID
        await client.send_message(
            chat_id=log_channel,
            text=f"#NewUser\n\nIᴅ - {user.id}\nNᴀᴍᴇ - {message.from_user.mention}"
        )

    reply_markup = InlineKeyboardMarkup(main_buttons)
    current_time = datetime.now(pytz.timezone(TIMEZONE))
    curr_time = current_time.hour        
    if curr_time < 12:
        gtxt = "ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🌞" 
    elif curr_time < 17:
        gtxt = "ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ 🌗" 
    elif curr_time < 21:
        gtxt = "ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ 🌘"
    else:
        gtxt = "ɢᴏᴏᴅ ɴɪɢʜᴛ 🌑"
    
    await client.send_message(
        chat_id=message.chat.id,
        text=Translation.START_TXT.format(message.from_user.mention, gtxt),
        reply_markup=reply_markup
    )

#==================Restart Function==================#

@Client.on_message(filters.private & filters.command(['restart']) & filters.user(Config.BOT_OWNER_ID))
async def restart(client, message):
    msg = await message.reply_text(
        text="<i>Trying to restarting.....</i>"
    )
    await asyncio.sleep(5)
    await msg.edit("<i>Server restarted successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)
    
#==================Callback Functions==================#

@Client.on_callback_query(filters.regex(r'^help'))
async def helpcb(bot, query):
    await query.message.edit_text(
        text=Translation.HELP_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('• ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ?', callback_data='how_to_use')
            ],[
            InlineKeyboardButton('• sᴇᴛᴛɪɴɢs', callback_data='settings#main'),
            InlineKeyboardButton('• sᴛᴀᴛᴜs ', callback_data='status')
            ],[
            InlineKeyboardButton('• ʙᴀᴄᴋ', callback_data='back'),
            InlineKeyboardButton('• ᴀʙᴏᴜᴛ', callback_data='about')
            ]]
        ))

@Client.on_callback_query(filters.regex(r'^how_to_use'))
async def how_to_use(bot, query):
    await query.message.edit_text(
        text=Translation.HOW_USE_TXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('• ʙᴀᴄᴋ', callback_data='help')]]),
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex(r'^back'))
async def back(bot, query):
    reply_markup = InlineKeyboardMarkup(main_buttons)
    current_time = datetime.now(pytz.timezone(TIMEZONE))
    curr_time = current_time.hour        
    if curr_time < 12:
        gtxt = "ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🌞" 
    elif curr_time < 17:
        gtxt = "ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ 🌗" 
    elif curr_time < 21:
        gtxt = "ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ 🌘"
    else:
        gtxt = "ɢᴏᴏᴅ ɴɪɢʜᴛ 🌑"
    
    await query.message.edit_text(
        text=Translation.START_TXT.format(query.from_user.mention, gtxt),
        reply_markup=reply_markup
    )

        
@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    await query.message.edit_text(
        text=Translation.ABOUT_TXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('• ʙᴀᴄᴋ', callback_data='back')]])
    )

@Client.on_callback_query(filters.regex(r'^donate'))
async def donate(bot, query):
    await query.message.edit_text(
        text=Translation.DONATE_TXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('• ʙᴀᴄᴋ', callback_data='back')]])
    )

@Client.on_callback_query(filters.regex(r'^status'))
async def status(bot, query):
    users_count, bots_count = await db.total_users_bots_count()
    total_channels = await db.total_channels()
    await query.message.edit_text(
        text=Translation.STATUS_TXT.format(users_count, bots_count, temp.forwardings, total_channels, temp.BANNED_USERS ),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('• ʙᴀᴄᴋ', callback_data='help')]]),
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )
@Client.on_message(filters.private & filters.command(['stats']) & filters.user(Config.BOT_OWNER_ID))
async def stats(client, message):
    users_count, bots_count = await db.total_users_bots_count()
    total_channels = await db.total_channels()
    await client.send_message(
        chat_id=message.chat.id,
        text=Translation.STATUS_TXT.format(users_count, bots_count, temp.forwardings, total_channels, temp.BANNED_USERS )
    )

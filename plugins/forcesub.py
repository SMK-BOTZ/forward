import asyncio
from config import Config
import pyrogram
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery


async def ForceSub(c: Client, m: Message):
    try:
        invite_link = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        invite_link = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
    except Exception as err:
        print(f"Unable to create invite link for {Config.UPDATES_CHANNEL}\n\nError: {err}")
        return 200
    try:
        user = await c.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=m.from_user.id)
        if user.status == "kicked":
            await c.send_message(
                chat_id=m.from_user.id,
                text="Sorry, you are banned from using this bot. Contact my admin @VR_Necromancer.",
                disable_web_page_preview=True,
                parse_mode="Markdown",
            )
            return 400
    except UserNotParticipant:
        await c.send_message(
            chat_id=m.from_user.id,
            text="**Please join my updates channel to use this bot!**\n\nOnly channel subscribers can use the bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("• Join Channel", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("↻ Refresh", callback_data="refresh_subscription")
                    ]
                ]
            )
        )
        return 400
    except Exception:
        await c.send_message(
            chat_id=m.from_user.id,
            text="Something went wrong. Contact my admin.",
            disable_web_page_preview=True,
            parse_mode="Markdown",
        )
        return 400
    return 200


@Client.on_callback_query(filters.regex("refresh_subscription"))
async def refresh_subscription(c: Client, callback_query: CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        chat_id = (int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL)
        
        user = await c.get_chat_member(chat_id=chat_id, user_id=user_id)
        if user.status in ["member", "administrator", "creator"]:
            await callback_query.message.edit_text(
                text="🎉 You have successfully subscribed! You can now use the bot.",
                reply_markup=None
            )
        else:
            raise UserNotParticipant
    except UserNotParticipant:
        await callback_query.answer(
            text="You are not subscribed yet! Please join the channel and try again.",
            show_alert=True
        )
    except Exception as e:
        print(f"Error during refresh: {e}")
        await callback_query.answer(
            text="Something went wrong. Please contact the admin.",
            show_alert=True
        )

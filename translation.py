import os
from config import Config

class Translation(object):
  START_TXT = """<b>ʜɪ {}

ɪ'ᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴛᴏ ꜰᴏʀᴡᴀʀᴅ ʙᴏᴛ
ɪ ᴄᴀɴ ꜰᴏʀᴡᴀʀᴅ ᴀʟʟ ᴍᴇssᴀɢᴇ ꜰʀᴏᴍ ᴏɴᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴄʜᴀɴɴᴇʟ

ᴄʟɪᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ</b>"""


  HELP_TXT = """<b><u>🔆 HELP</u>

📚 Available commands:
⏣ /start - check I'm alive 
⏣ /forward - forward messages
⏣ /private_forward - forward messages from private chat
⏣ /unequify - delete duplicate media messages in chats
⏣ /settings - configure your settings
⏣ /stop - stop your ongoing tasks
⏣ /reset - reset your settings

💢 Features:
► Forward message from public channel to your channel without admin permission. if the channel is private need admin permission
► Forward message from private channel to your channel by using userbot(user must be member in there)
► custom caption
► custom button
► support restricted chats
► skip duplicate messages
► filter type of messages
► skip messages based on extensions & keywords & size</b>
"""
  
  HOW_USE_TXT = """<b><u>⚠️ Before Forwarding:</b></u>
► First add a bot or userbot
► add atleast one target channel <code>(your bot/userbot must be admin in there)</code>
► You can add chats or bots by using /settings
► if the Source Channel is private your userbot must be member in there or your bot must need admin permission in there also
► Then use /forward to forward messages</b>"""
  
  ABOUT_TXT = """<b>╔════❰ ғᴏʀᴡᴀʀᴅ ʙᴏᴛ ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ʙᴏᴛ : <a href=https://t.me/VR_Forward_Bot>ꜰᴏʀᴡᴀʀᴅ ʙᴏᴛ</a>
║┣⪼👦ᴄʀᴇᴀᴛᴏʀ : <a href=https://t.me/VR_Necromancer>ɴᴇᴄʀᴏᴍᴀɴᴄᴇʀ</a>
║┣⪼📡ʜᴏsᴛᴇᴅ ᴏɴ : ᴀʟᴘʜᴀ ᴠʀ
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ3
║┣⪼📚ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ ᴀsʏɴᴄɪᴏ 2.0.0 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : 2.4.2
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪</b>"""

  DONATE_TXT = """if you liked me ❤️. consider make a donation to support my developer 👦

UPI ID - <code>mohammedrznx@fam</code>"""  

  STATUS_TXT = """<b>╔════❰ ʙᴏᴛ sᴛᴀᴛᴜs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼👱 ᴛᴏᴛᴀʟ ᴜsᴇʀs: {}
║┃
║┣⪼🤖 ᴛᴏᴛᴀʟ ʙᴏᴛ: {}
║┃
║┣⪼🔃 ғᴏʀᴡᴀʀᴅɪɴɢs: {}
║┃
║┣⪼🔍 ᴜɴᴇǫᴜɪꜰʏɪɴɢs: {}
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
</b>""" 
  
  FROM_MSG = "<b>❪ SET SOURCE CHAT ❫\n\nForward the last message or last message link of source chat.\n/cancel - cancel this process</b>"
  TO_MSG = "<b>❪ CHOOSE TARGET CHAT ❫\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"
  SKIP_MSG = "<b>❪ SET MESSAGE SKIPING NUMBER ❫</b>\n\n<b>Skip the message as much as you enter the number and the rest of the message will be forwarded\nDefault Skip Number =</b> <code>0</code>\n<code>eg: You enter 0 = 0 message skiped\n You enter 5 = 5 message skiped</code>\n/cancel <b>- cancel this process</b>"
  CANCEL = "<b>Process Cancelled Succefully !</b>"
  BOT_DETAILS = "<b><u>📄 BOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"
  USER_DETAILS = "<b><u>📄 USERBOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"  
         
  TEXT = """<b>╭────❰ <u>Forwarded Status</u> ❱────❍
┃
┣⊸<b>🕵 ғᴇᴄʜᴇᴅ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>✅ sᴜᴄᴄᴇғᴜʟʟʏ ғᴡᴅ :</b> <code>{}</code>
┣⊸<b>👥 ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>🗑️ ᴅᴇʟᴇᴛᴇᴅ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>🪆 sᴋɪᴘᴘᴇᴅ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>📊 sᴛᴀᴛᴜs  :</b> <code>{}</code>
┣⊸<b>⏳ ᴘʀᴏɢʀᴇss  :</b> <code>{}</code> %
┣⊸<b>⏰ ᴇᴛᴀ :</b> <code>{}</code>
┃
╰────⌊ <b>{}</b> ⌉───❍</b>"""

  TEXT1 = """
╔════❰ ғᴏʀᴡᴀʀᴅ sᴛᴀᴛᴜs ❱➠
║╭━━━━━━━━━━━━━━━➣
║┃
║┣⪼**🕵 ғᴇᴄʜᴇᴅ ᴍsɢ :** `{}`
║┃
║┣⪼**✅ sᴜᴄᴄᴇғᴜʟʟʏ ғᴡᴅ :** `{}`
║┃
║┣⪼**👥 ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍsɢ :** `{}`
║┃
║┣⪼**🗑️ ᴅᴇʟᴇᴛᴇᴅ ᴍsɢ :** `{}`
║┃
║┣⪼**🪆 sᴋɪᴘᴘᴇᴅ ᴍsɢ :** `{}`
║┃
║┣⪼**📊 sᴛᴀᴛᴜs  :** `{}`
║┃
║┣⪼**⏳ ᴘʀᴏɢʀᴇss :** `{}`
║┃
║┣⪼**⏰ ᴇᴛᴀ :** `{}`
║┃
║╰━━━━━━━━━━━━━━━➣ 
╚════❰ **{}** ❱➠ """

  DUPLICATE_TEXT = """
╔════❰ ᴜɴᴇǫᴜɪғʏ sᴛᴀᴛᴜs ❱
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>ғᴇᴛᴄʜᴇᴅ ғɪʟᴇs:</b> <code>{}</code>
║┃
║┣⪼ <b>ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴅᴇʟᴇᴛᴇᴅ:</b> <code>{}</code> 
║╰━━━━━━━━━━━━━━━➣
╚════❰ ❱
"""
  DOUBLE_CHECK = """<b><u>DOUBLE CHECKING ⚠️</b></u>
<code>Before forwarding the messages Click the Yes button only after checking the following</code>

<b>★ YOUR BOT:</b> [{botname}](t.me/{botuname})
<b>★ FROM CHANNEL:</b> `{from_chat}`
<b>★ TO CHANNEL:</b> `{to_chat}`
<b>★ SKIP MESSAGES:</b> `{skip}`

<i>° [{botname}](t.me/{botuname}) must be admin in **TARGET CHAT**</i> (`{to_chat}`)
<i>° If the **SOURCE CHAT** is private your userbot must be member or your bot must be admin in there also</b></i>

<b>If the above is checked then the yes button can be clicked</b>"""

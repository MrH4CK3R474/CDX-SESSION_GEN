from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/6096e57658e6e395a3edc.jpg", caption=f"☞ Fɪʀsᴛ Yᴏᴜ Nᴇᴇᴅ ᴛᴏ Jᴏɪɴ Oᴜʀ Nᴇᴛᴡᴏʀᴋ ᴛᴏ Usᴇ ᴛʜɪs Bᴏᴛ Eғғɪᴄɪᴇɴᴛʟʏ. /start Aɢᴀɪɴ Aғᴛᴇʀ Jᴏɪɴɪɴɢ !",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🏴‍☠ ɴᴇᴛᴡᴏʀᴋ 🏴‍☠", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")

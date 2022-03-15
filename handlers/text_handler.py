from aiogram import types
from misc import dp, bot
import asyncio

ADMIN_ID_1 = 1307813926  # КСЮ
chatPost = -1001610117751


@dp.message_handler(content_types=['text', 'voice', 'video', 'video_note'])
async def all_other_messages(message: types.message):
    if message.chat.id == ADMIN_ID_1:
        markup = types.InlineKeyboardMarkup()
        bat_1 = types.InlineKeyboardButton(text='смотреть фулл🥵', url=message.text)
        bat_2 = types.InlineKeyboardButton(text='маленькая пися🥰', url=message.text)
        markup.add(bat_1)
        markup.add(bat_2)

        link = message.text

        """ОПРАВЛЯЕМ ОСНОВНОЙ ПОСТ"""
        await bot.copy_message(from_chat_id=chatPost, chat_id=message.chat.id, message_id=2, caption=f"""
<b>👧 Prиvate </b><b><a href = '{link}'>Pornhub</a></b><b> Channel 👼</b>

<i>этот и куча других <a href = '{link}'>ебабельных</a> фуллов
🍪🍼🐱🍑🍒🍆💦🩸🔞♋️🏳️‍🌈🏳️‍⚧️</i>

👇 <a href = '{link}'>9999</a> ГБ популярного порно 👇

🌐 <b>Канал:</b> <b>{link}</b> 🌐

❤️ <b><a href = '{link}'>Зайдите и оргазмуйте ❤️</a></b>

""", parse_mode='html', reply_markup=markup)

        await bot.send_message(chat_id=message.chat.id,text=f"""
<b>👶🏼 МИЛУЮ ЛОЛЮ ВЫЕБАЛИ ДВА ПАПИНЫХ ДРУГА НА ПЬЯНКЕ🍼</b>

<b>{link}</b>

❌ ❌ ВСЕ БЕГОМ <a href = '{link}'>СЮДА☝️</a>  (Могут снести)😱""")

        await bot.send_message(chat_id= message.chat.id, text=f"""
<b>Еблю миленьких писюх сливаю в этот канал.. 🍪..Это пиздец..

<i>{link}</i></b>
""")
        await bot.send_message(chat_id=message.chat.id, text=f"""
<b>⚠️Вас упомянул администратор канала:

<i>{link}</i></b>""")

        await bot.send_message(chat_id=message.chat.id, text=f"""
<b>🙊Сочно сосет член друга😈
— {link}

😈Девственницы💦👇🏼
— {link}</b>""")


        await bot.send_message(chat_id=message.chat.id,text=f""" 
<b>🔐 zапреtный архиv [21+🐰]
<i>{link}</i>

🐥🩸лишение целок (frst sx)
<i>{link}</i>

💞ПИЗДАТЫЙ КОНТЕНТ ИЗ Д@РkНЕТА:
<i>{link}</i></b>""")


        await bot.copy_message(from_chat_id=chatPost,chat_id=message.chat.id, message_id = 9, caption=f"""
🗃🥀356ГБ ЛЮБИМОГО ВОЗРАСТА🌺🩸🔞💦
<b>🌒АРХИВ👇</b>
{link}
БЕСПЛАТНЫЙ АРХИВ БЫСТРЕЕ 🇷🇺""")

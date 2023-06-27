from aiogram import types
import wikipedia

from loader import dp

wikipedia.set_lang("uz")
# Echo bot
@dp.message_handler(state=None)
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi')




from aiogram import types
import wikipedia

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    wikipedia.set_lang("uz")
    savol = message.text
    javob = wikipedia.summary(savol)

    await message.answer(javob)

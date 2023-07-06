# test_simple_chat_bot
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import  Message


API_TOKEN: str = '5822431030:AAH0DsNkD1COsdRnlXTGSq22a5f-vzHUOIc'

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()

@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет')

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Чем могу помочь')

@dp.message(F.photo)
async def send_photo(message: types.Message):
    await message.reply_photo(message.photo[-1].file_id)


@dp.message(F.video)
async def send_video(message: types.Message):
    await message.reply_video(message.video.file_id)


@dp.message(F.audio)
async def send_audio(message: types.Message):
    await message.reply_audio(message.audio.file_id)

@dp.message(F.voice)
async def exo_voice(message: Message):
    await message.reply_voice(message.voice.file_id)

@dp.message(F.sticker)
async def send_stiker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)




@dp.message()
async def process_answer_another_text(message: Message):
    await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)

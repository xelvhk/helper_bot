from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import helper_kb, task_kb, weather_kb
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=helper_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=helper_kb)



# Эти хэндлеры срабатывают на любую из кнопок
@router.message(F.text.in_([LEXICON_RU['weather']]))
async def process_game_button(message: Message):
    await message.answer(text=LEXICON_RU['weather_answer'],
                         reply_markup=weather_kb)
    
@router.message(F.text.in_([LEXICON_RU['tasks']]))
async def process_game_button(message: Message):
    await message.answer(text=LEXICON_RU['tasks_answer'],
                         reply_markup=weather_kb)
    
@router.message(F.text.in_([LEXICON_RU['happy']]))
async def process_game_button(message: Message):
    await message.answer(text=LEXICON_RU['happy_answer'],
                         reply_markup=weather_kb)
   
@router.message(F.text.in_([LEXICON_RU['back']]))
async def process_game_button(message: Message):
    await message.answer(text=LEXICON_RU['ready'],
                         reply_markup=helper_kb)
   
# Этот хэндлер будет срабатывать на команду "/placeholder"
@router.message(Command(commands='placeholder'))
async def process_placeholder_command(message: Message):
    await message.answer(
        text='Выберите что делать с задачами',
        reply_markup=task_kb
    )
from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import helper_kb, happy_kb, contacts_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_weather, get_joke,get_city_coordinates

router = Router()
bot = Bot


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=helper_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'],
                         reply_markup=helper_kb)


# Эти хэндлеры срабатывают на любую из кнопок
@router.message(F.text.in_([LEXICON_RU['ask_weather']]))
async def weather_command(message: Message):
    await message.reply(
        text="Пожалуйста, укажите город для получения погоды.")



@router.message(F.text.in_([LEXICON_RU['tasks']]))
async def process_tasks_button(message: Message):
    await message.answer(
        text="Используйте комманды для добавления, просмотра и удаления задач:\n /add_task - добавить,\n /show_task - посмотреть,\n /clear_task - удалить")


@router.message(F.text.in_([LEXICON_RU['happy']]))
async def process_happy_button(message: Message):
    await message.answer(text=LEXICON_RU['happy_answer'],
                         reply_markup=happy_kb)


@router.message(F.text.in_([LEXICON_RU['back']]))
async def process_back_button(message: Message):
    await message.answer(text=LEXICON_RU['ready'],
                         reply_markup=helper_kb)


# Этот хэндлер будет срабатывать на команду "/placeholder"
@router.message(Command(commands='placeholder'))
async def process_placeholder_command(message: Message):
    await message.answer(
        text='Выберите что делать с задачами',
    )

@router.message(lambda message: not message.text.startswith('/'))
async def get_weather_by_city(message: Message):
    city = message.text.strip()
    latitude, longitude = get_city_coordinates(city)
    if latitude and longitude:
        weather_report = get_weather(latitude, longitude)
        await message.reply(weather_report)
    else:
        await message.reply("Пожалуйста, укажите город, чтобы я мог вывести погоду.")


@router.message(F.text.in_([LEXICON_RU['gen_joke']]))
async def send_joke(message: Message):
    joke = get_joke()
    await message.reply(joke)


@router.message(F.text.in_([LEXICON_RU['contacts']]))
async def send_contacts(message: Message):
    await message.answer(text=LEXICON_RU['text_me'],
                         reply_markup=contacts_kb)

user_tasks = {}



@router.message(Command(commands='add_task'))
async def add_task(message: Message):
    task = message.text.replace('/add_task', '').strip()
    if task:
        user_id = message.from_user.id
        if user_id not in user_tasks:
            user_tasks[user_id] = []
        user_tasks[user_id].append(task)
        await message.reply(f"Задача '{task}' добавлена.")
    else:
        await message.reply("Кажется, задача пустая. Введите задачу после команды /add_task")


@router.message(Command(commands='show_task'))
async def list_tasks(message: Message):
    user_id = message.from_user.id
    if user_id in user_tasks and user_tasks[user_id]:
        tasks = "\n".join(f"{idx + 1}. {task}" for idx, task in enumerate(user_tasks[user_id]))
        await message.reply(f"Ваши задачи на день:\n{tasks}")
    else:
        await message.reply("У вас нет задач.")



@router.message(Command(commands='clear_task'))
async def clear_tasks(message: Message):
    user_id = message.from_user.id
    user_tasks[user_id] = []
    await message.reply("Все задачи удалены.")


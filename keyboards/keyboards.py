from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU


# Создаем кнопки клавиатуры
kb_button_1 = KeyboardButton(text=LEXICON_RU['weather'])
kb_button_2 = KeyboardButton(text=LEXICON_RU['tasks'])
kb_button_3 = KeyboardButton(text=LEXICON_RU['happy'])

# Создаем клавиатуру функций
helper_kb = ReplyKeyboardMarkup(
    keyboard=[[kb_button_1],
              [kb_button_2],
              [kb_button_3]],
    resize_keyboard=True
)

# Создаем объекты инлайн-кнопок для задач
task_button_1 = KeyboardButton(text=LEXICON_RU['add_task'])

task_button_2 = KeyboardButton(text=LEXICON_RU['show_task'])

task_button_3 = KeyboardButton(text=LEXICON_RU['back'])

# Создаем объект клавиатуры для задач
task_kb = ReplyKeyboardMarkup(
    keyboard=[[task_button_1],
              [task_button_2],
              [task_button_3]],
    resize_keyboard=True
)

weather_button_1 = KeyboardButton(text=LEXICON_RU['ask_weather'])
weather_button_2 = KeyboardButton(text=LEXICON_RU['back'])

weather_kb = ReplyKeyboardMarkup(
    keyboard=[[weather_button_1],
              [weather_button_2]],
    resize_keyboard=True,
    input_field_placeholder='Нажмите узнать погоду'
)
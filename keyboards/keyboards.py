from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU


# Создаем кнопки клавиатуры
kb_button_1 = KeyboardButton(text=LEXICON_RU['weather'])
kb_button_2 = KeyboardButton(text=LEXICON_RU['tasks'])
kb_button_3 = KeyboardButton(text=LEXICON_RU['happy'])
kb_button_4 = KeyboardButton(text=LEXICON_RU['contacts'])

# Создаем клавиатуру функций
helper_kb = ReplyKeyboardMarkup(
    keyboard=[[kb_button_1],
              [kb_button_2],
              [kb_button_3],
              [kb_button_4]],
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

happy_button_1 = KeyboardButton(text=LEXICON_RU['gen_joke'])
happy_button_2 = KeyboardButton(text=LEXICON_RU['back'])


happy_kb = ReplyKeyboardMarkup(
    keyboard=[[happy_button_1],
              [happy_button_2]],
    resize_keyboard=True,
    input_field_placeholder='Нажмите кнопку, чтобы сгенерировать шутку'
)

contacts_url_1 = InlineKeyboardButton(text='GitHub', url='https://github.com/xelvhk')
contacts_url_2 = InlineKeyboardButton(text='Telegram', url='https://t.me/hex_lex')
contacts_url_3 = InlineKeyboardButton(text='Instagram', url='https://instagram.com/days_of_nothing')

contacts_kb = InlineKeyboardMarkup(
    inline_keyboard=[[contacts_url_1],
                     [contacts_url_2],
                     [contacts_url_3]])


task_button_1 = InlineKeyboardButton(text=LEXICON_RU['add_task'], callback_data='add_task')
task_button_2 = InlineKeyboardButton(text=LEXICON_RU['show_task'], callback_data='show_task')
task_button_3 = InlineKeyboardButton(text=LEXICON_RU['clear_task'], callback_data='clear_task')

# Создаем объект клавиатуры для задач
tasks_kb = InlineKeyboardMarkup(
    keyboard=[[task_button_1],
              [task_button_2],
              [task_button_3]])

import random
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import helper_kb, task_kb, weather_kb

# Функция, возвращающая ключ из словаря, по которому
# хранится значение, передаваемое как аргумент - выбор пользователя 
def normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key

def select_point(user_answer: str) -> str:
    for key in LEXICON_RU:
        if user_answer == 'weather':
            return weather_kb
        elif user_answer == 'tasks':
            return task_kb
        else:
            return LEXICON_RU['other_answer']
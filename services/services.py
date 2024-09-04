import random
from lexicon.lexicon_ru import LEXICON_RU
import requests

# Для получения координат любого города
GEO_API_URL = "https://nominatim.openstreetmap.org/search?"

# Функция для получения координат города
def get_city_coordinates(city: str):
    params = {
        'q': city,
        'format': 'json',
        'limit': 1
    }
    response = requests.get(GEO_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
    return None, None

# Прогноз погоды по API
def get_weather(latitude: float, longitude: float) -> str:
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    print(weather_url)

    if weather_response.status_code == 200 and "current_weather" in weather_data:
        # Обработка полученной информации
        temperature = weather_data['current_weather']['temperature']
        wind_speed = weather_data['current_weather']['windspeed']
        weather_code = weather_data['current_weather']['weathercode']

        # Добавление описания
        weather_descriptions = {
            0: "Ясно. Понятно?",
            1: "Преимущественно ясно, но не очень",
            2: "Переменная облачность. Тучи. Но немного",
            3: "Пасмурно. Тучи, много туч",
            45: "Туман. Как обычно в Петербурге и в Лондоне",
            48: "Гололедный туман. Мало того, что туман, так и гололед",
            51: "Легкая морось. Капает, но мало",
            53: "Умеренная морось. Капает. Уже не мало",
            55: "Сильная морось. Сильно капает",
            56: "Легкая ледяная морось. Замерзло и капает",
            57: "Сильная ледяная морось. Замерзло и сильно капает",
            61: "Небольшой дождь. Норм, без зонта",
            63: "Умеренный дождь. Нужен зонт",
            65: "Сильный дождь. Сиди дома",
            66: "Легкий ледяной дождь",
            67: "Сильный ледяной дождь. Не просто дождь, а ледяной!",
            71: "Небольшой снегопад. Чуть-чуть",
            73: "Умеренный снегопад. Снег, но не прямо много",
            75: "Сильный снегопад. Очень много снега",
            77: "Снежные зерна",
            80: "Небольшие ливни. Когда льёт как из ведра, но маленького",
            81: "Умеренные ливни. Когда льёт как из ведра, среднего",
            82: "Сильные ливни. Когда льёт как из ведра, большого",
            85: "Снегопад и ливень",
            86: "Сильный снегопад и ливень. Ужас какой-то",
            95: "Гроза. Очень шумно",
            96: "Гроза с легким градом. Как будто одной грозы мало",
            99: "Гроза с сильным градом. Шумно и больно",
        }
        weather_description = weather_descriptions.get(weather_code, "Непонятная погода")

        weather_report = (
            f"Погода в городе сейчас такая:\n"
            f"Чего ждать: {weather_description}\n"
            f"Температура по цельсию: {temperature:.1f}°C\n"
            f"Скорость ветра: {wind_speed:.1f} м/с"
        )
    else:
        weather_report = "Не могу понять, что за погода"

    return weather_report

# Генерация шуток v.1
# words_list = [
#     "шутку", "информатику", "телеграм", "бот", "айограм", "коворкинг", "программирование",
#     "python", "код", "разработку", "гитхаб", "интернет", "плохую погоду",
#     "двойку по информатике", "несмешную шутку", "vs code"
# ]


# def get_joke():
#     selected_words = random.simple(words_list, 3)
#     joke_one = f"Что получится, если соединить {selected_words[0]} и {selected_words[1]}?"
#     joke_two = f"Немного {selected_words[2]} и много потраченного времени!"
#     return joke_one + joke_two

# Генерация шуток v.2
words1 = ['человек', 'столб', 'дом']
words2 = ['шёл', 'летел', 'плыл']
words3 = ['под водой', 'по лесу', 'высоко над облаками']
words4 = ['и упал', 'и споткнулся', 'и стал рыбой']


def get_joke():
    selected_1 = ' '.join(random.sample(words1, 1))
    selected_2 = ' '.join(random.sample(words2, 1))
    selected_3 = ' '.join(random.sample(words3, 1))
    selected_4 = ' '.join(random.sample(words4, 1))
    joke = f"{selected_1} {selected_2} {selected_3} {selected_4}"
    return joke

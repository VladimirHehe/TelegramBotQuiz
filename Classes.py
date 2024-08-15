import telebot
from telebot import types
from config import conf

bot = telebot.TeleBot(conf())


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.send_message(message.chat.id, '⭐️Добро пожаловать в бот-викторину Московского Зоопарка!⭐️',
                     reply_markup=get_start_keyboard())


def get_start_keyboard():
    markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton("Начать Викторину ➡️")
    button_2 = types.KeyboardButton("❓ Помощь")
    markup_start.add(button_1, button_2)
    return markup_start


def time(message):
    i = 0
    import time
    while i < 3:
        if i == 0:
            mes1 = bot.send_message(chat_id=message.chat.id, text="1️⃣")
            time.sleep(0.5)
            bot.delete_message(chat_id=message.chat.id, message_id=mes1.id)
            i += 1
        if i == 1:
            mes2 = bot.send_message(chat_id=message.chat.id, text="2️⃣")
            time.sleep(0.5)
            bot.delete_message(chat_id=message.chat.id, message_id=mes2.id)
            i += 1
        if i == 2:
            mes3 = bot.send_message(chat_id=message.chat.id, text="3️⃣")
            time.sleep(0.5)
            bot.delete_message(chat_id=message.chat.id, message_id=mes3.id)
            i += 1


questions = {
    1: {
        'question': "Какое животные нравится вам больше?",
        'options': ["Рысь", "Панда", "Тигр", "Альпака"],
        'correct_answer': 2,
        'photo_url': 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/71062cdc-ae27-432a-84ed-d3743afd903b.jpeg'
    },
    2: {
        'question': "Как думаете, что это за животное?",
        'options': ["Утка", "Лебедь", "Бобр", "Утконос"],
        'correct_answer': 3,
        'photo_url': 'https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F4c%2F42%2F28%2F4c4228ce4068a37c826becc94e63add2.jpg&lr=55&p=1&pos=19&rpt=simage&text=утконос'
    },
    3: {
        'question': "В каком был открыт наш Зоопарк?",
        'options': ["2001", "1936", "1898", "1864"],
        'correct_answer': 3,
        'photo_url': 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/about_home/9083907d-fef0-48ff-a70d-292e2272f329.jpg'
    },
    4: {
        'question': "Чего из этого у нас нет?",
        'options': ["Мастер-класс по акварелям", "Сыграть свадьбу", "Плохого обращения с животными",
                 "Множества милых животных"],
        'correct_answer': 2,
        'photo_url': 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/about_home/9083907d-fef0-48ff-a70d-292e2272f329.jpg'
    },
    5: {
        'question': "Сколько видов животных обитает в Московском Зоопарке?",
        'options': ["Около 550", "Около 1100", "Около 1600",
                 "Более 2000"],
'correct_answer': 1,
        'photo_url': 'https://new.moscowzoo.ru/assets/img/manul-cave.gif'
    },
    6: {
        'question': "Какая птица является символом Московского Зоопарка и частым участником парадов и праздников?",
        'options': ["Птенцы", "Павлины", "Феникс",
                 "Журавли"],
        'correct_answer': 1,
        'photo_url': 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/71062cdc-ae27-432a-84ed-d3743afd903b.jpeg'
    },
    7: {
        'question': "Как зовут медведя-самца, который был одним из самых популярных обитателей Московского зоопарка и скончался в 2017 году?",
        'options': ["Миша", "Барсик", "Вася",
                 "Шарик"],
        'correct_answer': 0,
        'photo_url': 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/71062cdc-ae27-432a-84ed-d3743afd903b.jpeg'
    },
    8: {
        'question': "Какой праздник отмечается в Московском зоопарке 1 марта в честь всех зверей?",
        'options': ["День всех животных", "День всех рыб", "День зоо",
                 "День всех кошек"],
        'correct_answer': 3,
        'photo_url': 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/about_home/9083907d-fef0-48ff-a70d-292e2272f329.jpg'
    },
    9: {
        'question': "Какое животное является символом Московского Зоопарка?",
        'options': ["Манул", "Сибирский кот", "Рысь",
                 "Медведь"],
        'correct_answer': 0,
        'photo_url': 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/71062cdc-ae27-432a-84ed-d3743afd903b.jpeg'
    },
    10: {
        'question': "Какой самый крупный вид обезьян проживает в Московском зоопарке?",
        'options': ["Шимпанзе", "Орангутаны", "Гориллы",
                 "Бонобо"],
        'correct_answer': 2,
        'photo_url': 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/71062cdc-ae27-432a-84ed-d3743afd903b.jpeg'
    }
}

@bot.message_handler(content_types=['text'])
def quiz_open_func(message: telebot.types.Message):
    if message.text == 'Начать Викторину ➡️':
        text_info = """ 
        Викторина о животных и Московском Зоопарке 
        ❔ 10 Вопросов   ⏰60с наответ"""
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Я готов(а)", callback_data='Ready'))
        bot.send_message(chat_id=message.chat.id, text=text_info, reply_markup=markup)

    elif message.text == '❓ Помощь':
        text_help = "Привет. Ты в разделе помощи!🆘\n" \
                    "\n" \
                    "Если хочешь узнать подробную информацию или посетить официальный телеграмм или сайт - переходи в профиль бота!\n" \
                    "\n" \
                    "Для начала Викторины нажми на кнопку 'Начать Викторину ➡️'" \
                    "❤️ На этом всё. Очень просто :3 ❤️"

        return bot.send_message(message.chat.id, text_help)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query1(call: telebot.types.CallbackQuery):
    if call.data == "Ready":
        time(call.message)
        current_question = 1
        send_question(bot, call.message, current_question)
    if call.data.startswith('question'):
        current_question = int(call.data.split('_')[1]) + 1
        send_question(bot, call.message, current_question)


def send_question(bot, message, current_question):
    question_data = questions[current_question]
    markup = types.InlineKeyboardMarkup()
    markup.add(
        *[types.InlineKeyboardButton(text=option, callback_data=f'question_{current_question}_{index}') for index, option in
          enumerate(question_data['options'])]
    )
    bot.send_photo(message.chat.id, photo=question_data['photo_url'], caption=question_data['question'],
                   reply_markup=markup, parse_mode='Markdown')

bot.polling(none_stop=True)
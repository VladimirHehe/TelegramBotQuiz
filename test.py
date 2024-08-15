import telebot
from telebot import types
from config import conf

bot = telebot.TeleBot(conf())

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


@bot.message_handler(content_types=['text'])
def quiz_open_func(message: telebot.types.Message):
    if message.text == 'Начать Викторину ➡️':
        text_info = """ 
        Викторина о животных и Московском Зоопарке 
        ❔ 10 Вопросов   ⏰60с на ответ"""
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
        quiz_start(call.message)
    if call.data == "question2":
        question2(call.message)
    if call.data == "question3":
        question3(call.message)
    if call.data == "question4":
        question4(call.message)
    if call.data == "question5":
        question5(call.message)
    if call.data == "question6":
        question6(call.message)
    if call.data == "question7":
        question7(call.message)
    if call.data == "question8":
        question8(call.message)
    if call.data == "question9":
        question9(call.message)
    if call.data == "question10":
        question10(call.message)
    if call.data == "question_end_print":
        finally_(call.message)


@bot.message_handler(content_types=['text'])
def quiz_start(message: telebot.types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Дальше", callback_data='question2', ))
    bot.send_poll(message.chat.id, question="[1/10] Какое животные нравится вам больше?",
                  options=["Рысь", "Панда", "Тигр", "Альпака"], is_anonymous=False, open_period=60,
                  allows_multiple_answers=False, reply_markup=markup)


def question2(message: telebot.types.Message):
    bot.send_photo(message.chat.id,
                   'https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F4c%2F42%2F28%2F4c4228ce4068a37c826becc94e63add2.jpg&lr=55&p=1&pos=19&rpt=simage&text=утконос')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Дальше", callback_data='question3'))
    bot.send_poll(message.chat.id, question=f"[2/10] Как думаете, что это за животное?",
                  options=["Утка", "Лебедь", "Бобр", "Утконос"], is_anonymous=False, type="quiz", correct_option_id=3,
                  explanation="Подсказка: Кто-то слышал про Финеса и Ферба?", open_period=60, reply_markup=markup, )


def question3(message: telebot.types.Message):
    bot.send_photo(message.chat.id,
                   'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/about_home/9083907d-fef0-48ff-a70d-292e2272f329.jpg')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Дальше", callback_data='question4'))
    bot.send_poll(message.chat.id, question=f"[3/10] В каком был открыт наш Зоопарк?",
                  options=["2001", "1936", "1898", "1864"], is_anonymous=False, type="quiz", correct_option_id=3,
                  explanation="Подсказка:Это было достаточно давно...", open_period=60, reply_markup=markup, )


def question4(message: telebot.types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Дальше", callback_data='question5'))
    bot.send_poll(message.chat.id, question=f"[4/10] Чего из этого у нас нет?",
                  options=["Мастер-класс по акварелям", "Сыграть свадьбу", "Плохого обращения с животными",
                           "Множества милых животных"], is_anonymous=False, type="quiz", correct_option_id=2,
                  explanation="Подсказка:Тут догадаться несложно, мы любим животных!", open_period=60,
                  reply_markup=markup, )


def question5(message: telebot.types.Message):
    bot.send_video(message.chat.id,
                   'https://new.moscowzoo.ru/assets/img/manul-cave.gif')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Дальше", callback_data='question6'))
    bot.send_poll(message.chat.id, question=f"[5/10]Сколько видов животных обитает в Московском Зоопарке?",
                  options=["Около 550", "Около 1100", "Около 1600",
                           "Более 2000"], is_anonymous=False, type="quiz", correct_option_id=1,
                  explanation="Подсказка:Не больше 1500", open_period=60, reply_markup=markup, )


def question6(message: telebot.types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Дальше", callback_data='question7'))
    bot.send_poll(message.chat.id,
                  question=f"[6/10] Какая птица является символом Московского Зоопарка и частым участником парадов и праздников?",
                  options=["Птенцы", "Павлины", "Феникс",
                           "Журавли"], is_anonymous=False, type="quiz", correct_option_id=1,
                  explanation="Подсказка: Очень грациозная птица!", open_period=60, reply_markup=markup, )


def question7(message: telebot.types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Дальше", callback_data='question8'))
    bot.send_poll(message.chat.id,
                  question=f"[7/10] Как зовут медведя-самца, который был одним из самых популярных обитателей Московского зоопарка и скончался в 2017 году?",
                  options=["Миша", "Барсик", "Вася",
                           "Шарик"], is_anonymous=False, type="quiz", correct_option_id=0,
                  explanation="Подсказка: В одном мультике девочка так называла медведя.", open_period=60,
                  reply_markup=markup, )


def question8(message: telebot.types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Дальше", callback_data='question9'))
    bot.send_poll(message.chat.id,
                  question=f"[8/10] Какой праздник отмечается в Московском зоопарке 1 марта в честь всех зверей?",
                  options=["День всех животных", "День всех рыб", "День зоо",
                           "День всех кошек"], is_anonymous=False, type="quiz", correct_option_id=3,
                  explanation="Подсказка:Этих животных любили в древнем Египте ", open_period=60, reply_markup=markup, )


def question9(message: telebot.types.Message):
    bot.send_photo(message.chat.id, 'https://i.pinimg.com/originals/ea/f9/ea/eaf9ea37aeed63f741c9666d1ca2bd9d.jpg')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Дальше", callback_data='question10'))
    bot.send_poll(message.chat.id,
                  question=f"[9/10]Какое животное является символом Московского Зоопарка?",
                  options=["Манул", "Сибирский кот", "Рысь",
                           "Медведь"], is_anonymous=False, type="quiz", correct_option_id=0,
                  explanation="Подсказка:Семейство кошачьих, начинается на 'М'", open_period=60, reply_markup=markup, )


def question10(message: telebot.types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Дальше", callback_data='question_end_print'))
    bot.send_poll(message.chat.id,
                  question=f"[10/10]Какой самый крупный вид обезьян проживает в Московском зоопарке?",
                  options=["Шимпанзе", "Орангутаны", "Гориллы",
                           "Бонобо"], is_anonymous=False, type="quiz", correct_option_id=2,
                  explanation="Подсказка:Есть с таким же название напиток", open_period=60, reply_markup=markup, )


def finally_(message: telebot.types.Message):
    import random
    import time
    result = random.randint(1, 10)
    if result == 1:
        markup = types.InlineKeyboardMarkup()
        item2 = types.InlineKeyboardButton("Пройти викторину ещё раз", callback_data="Ready")
        item1 = types.InlineKeyboardButton("Поделиться результатом", switch_inline_query="Я манул, а кто ты?")
        markup.add(item2, item1)
        photo_url = "https://www.rosphoto.com/images/u/articles/1602/5-larisa-kibardina.jpg"
        bot.send_photo(message.chat.id, caption='Ура! Ты манул!', photo=photo_url, reply_markup=markup)
        time.sleep(1)
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("Подробнее...", url="https://moscowzoo.ru/my-zoo/become-a-guardian/"))
        bot.send_message(message.chat.id, "❤️Ты можешь стать опекуном своего животного!❤️", reply_markup=markup1)

    if result == 2:
        markup = types.InlineKeyboardMarkup()
        item2 = types.InlineKeyboardButton("Пройти викторину ещё раз", callback_data="Ready")
        item1 = types.InlineKeyboardButton("Поделиться результатом", switch_inline_query="Я амурский тигр, а кто ты?")
        markup.add(item2, item1)
        photo_url = "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/71062cdc-ae27-432a-84ed-d3743afd903b.jpeg"
        bot.send_photo(message.chat.id, caption='Ура! Ты Амурский Тигр!', photo=photo_url, reply_markup=markup)
        time.sleep(1)
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("Подробнее...", url="https://moscowzoo.ru/my-zoo/become-a-guardian/"))
        bot.send_message(message.chat.id, "❤️Ты можешь стать опекуном своего животного!❤️", reply_markup=markup1)
    if result == 3:
        markup = types.InlineKeyboardMarkup()
        item2 = types.InlineKeyboardButton("Пройти викторину ещё раз", callback_data="Ready")
        item1 = types.InlineKeyboardButton("Поделиться результатом", switch_inline_query='Я гоголь, а кто ты?')
        markup.add(item2, item1)
        photo_url = "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/4a8ae509-335d-404f-ab21-70901a9c745a.jpeg"
        bot.send_photo(message.chat.id, caption='Ура! Ты Гоголь!', photo=photo_url, reply_markup=markup)

        time.sleep(1)
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("Подробнее...", url="https://moscowzoo.ru/my-zoo/become-a-guardian/"))
        bot.send_message(message.chat.id, "❤️Ты можешь стать опекуном своего животного!❤️", reply_markup=markup1)
    if result == 4:
        markup = types.InlineKeyboardMarkup()
        item2 = types.InlineKeyboardButton("Пройти викторину ещё раз", callback_data="Ready")
        item1 = types.InlineKeyboardButton("Поделиться результатом", switch_inline_query="Я Трубкозуб, а кто ты?")
        markup.add(item2, item1)
        photo_url = "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/24e47b06-ec4f-4e68-8a92-cc6c6d6ab076.jpeg"
        bot.send_photo(message.chat.id, caption='Ура! Ты Трубкозуб!', photo=photo_url, reply_markup=markup)

        time.sleep(1)
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("Подробнее...", url="https://moscowzoo.ru/my-zoo/become-a-guardian/"))
        bot.send_message(message.chat.id, "❤️Ты можешь стать опекуном своего животного!❤️", reply_markup=markup1)
    if result == 5:
        markup = types.InlineKeyboardMarkup()
        item2 = types.InlineKeyboardButton("Пройти викторину ещё раз", callback_data="Ready")
        item1 = types.InlineKeyboardButton("Поделиться результатом", switch_inline_query="Я розовый какаду, а кто ты?")
        markup.add(item2, item1)
        photo_url = "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/47eb38a5-b36f-49c0-bbaa-4b26d4cc7e92.jpeg"
        bot.send_photo(message.chat.id, caption='Ура! Ты Розовый Какаду!', photo=photo_url, reply_markup=markup)

        time.sleep(1)
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("Подробнее...", url="https://moscowzoo.ru/my-zoo/become-a-guardian/"))
        bot.send_message(message.chat.id, "❤️Ты можешь стать опекуном своего животного!❤️", reply_markup=markup1)
    if result == 6:
        markup = types.InlineKeyboardMarkup()
        item2 = types.InlineKeyboardButton("Пройти викторину ещё раз", callback_data="Ready")
        item1 = types.InlineKeyboardButton("Поделиться результатом", switch_inline_query='Я филин, а кто ты?')
        markup.add(item2, item1)
        photo_url = "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/763a0d3c-a7da-4cf1-812e-f0677e3df808.jpeg"
        bot.send_photo(message.chat.id, caption='Ура! Ты Филин!', photo=photo_url, reply_markup=markup)

        time.sleep(1)
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("Подробнее...", url="https://moscowzoo.ru/my-zoo/become-a-guardian/"))
        bot.send_message(message.chat.id, "❤️Ты можешь стать опекуном своего животного!❤️", reply_markup=markup1)
    if result == 7:
        markup = types.InlineKeyboardMarkup()
        item2 = types.InlineKeyboardButton("Пройти викторину ещё раз", callback_data="Ready")
        item1 = types.InlineKeyboardButton("Поделиться результатом", switch_inline_query='Я морж, а кто ты?')
        markup.add(item2, item1)
        photo_url = "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/3198de3d-df5f-47a2-9abe-529d2ef11623.jpeg"
        bot.send_photo(message.chat.id, caption='Ура! Ты Морж!', photo=photo_url, reply_markup=markup)

        time.sleep(1)
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("Подробнее...", url="https://moscowzoo.ru/my-zoo/become-a-guardian/"))
        bot.send_message(message.chat.id, "❤️Ты можешь стать опекуном своего животного!❤️", reply_markup=markup1)
    if result == 8:
        markup = types.InlineKeyboardMarkup()
        item2 = types.InlineKeyboardButton("Пройти викторину ещё раз", callback_data="Ready")
        item1 = types.InlineKeyboardButton("Поделиться результатом", switch_inline_query="Я медоед, а кто ты?")
        markup.add(item2, item1)
        photo_url = "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/16cb2d06-ecce-4e44-a01c-f6d7ba40be5f.jpeg"
        bot.send_photo(message.chat.id, caption='Ура! Ты Медоед!', photo=photo_url, reply_markup=markup)

        time.sleep(1)
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("Подробнее...", url="https://moscowzoo.ru/my-zoo/become-a-guardian/"))
        bot.send_message(message.chat.id, "❤️Ты можешь стать опекуном своего животного!❤️", reply_markup=markup1)
    if result == 9:
        markup = types.InlineKeyboardMarkup()
        item2 = types.InlineKeyboardButton("Пройти викторину ещё раз", callback_data="Ready")
        item1 = types.InlineKeyboardButton("Поделиться результатом", switch_inline_query='Я белый медведь, а кто ты?')
        markup.add(item2, item1)
        photo_url = "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/22c1783b-0644-434d-9b35-2143c5505033.jpeg"
        bot.send_photo(message.chat.id, caption='Ура! Ты Белый Медведь!', photo=photo_url, reply_markup=markup)

        time.sleep(1)
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("Подробнее...", url="https://moscowzoo.ru/my-zoo/become-a-guardian/"))
        bot.send_message(message.chat.id, "❤️Ты можешь стать опекуном своего животного!❤️", reply_markup=markup1)
    if result == 10:
        markup = types.InlineKeyboardMarkup()
        item2 = types.InlineKeyboardButton("Пройти викторину ещё раз", callback_data="Ready")
        item1 = types.InlineKeyboardButton("Поделиться результатом", switch_inline_query='Я альпака, а кто ты?')
        markup.add(item2, item1)
        photo_url = "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/7ee94b22-86c4-4ae6-a583-00d4e61ea90d.jpeg"
        bot.send_photo(message.chat.id, caption='Ура! Ты Альпака!', photo=photo_url, reply_markup=markup)

        time.sleep(1)
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("Подробнее...", url="https://moscowzoo.ru/my-zoo/become-a-guardian/"))
        bot.send_message(message.chat.id, "❤️Ты можешь стать опекуном своего животного!❤️", reply_markup=markup1)


bot.polling(none_stop=True)

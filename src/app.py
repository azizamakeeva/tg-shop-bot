# - *- coding: utf- 8 - *-

import time
import random
import urllib
from time import sleep
from io import BytesIO
from datetime import datetime

import telebot
import SimpleQIWI
from SimpleQIWI import *
from telebot import types

import menu
import config

bot = telebot.TeleBot(config.token, parse_mode=None)
print("Start")

joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(str(message.chat.id))
        print("\nБот был запущен. ID: " + str(message.chat.id) +
              '    Дата/время: ' + str(datetime.now()))
        bot.send_message(message.chat.id,
                         "Добро пожаловать в Pineapple Shop❗️\n\n◼️ Здесь ты можешь воспользоваться всеми возможными  услугами\n\n◼Огромный выбор услуг и товаров")
        bot.send_message(message.from_user.id,
                         'Выберите нужный раздел: ', reply_markup=menu.start)
    elif message.chat.id == config.admin_id:
        print("\nБот был запущен. ID: " + str(message.chat.id) +
              '    Дата/время: ' + str(datetime.now()))
        bot.send_message(message.chat.id,
                         "Добро пожаловать в Pineapple Shop❗️\n\n◼️ Здесь ты можешь воспользоваться всеми возможными  услугами\n\n◼Огромный выбор услуг и товаров")
        bot.send_message(message.from_user.id,
                         'Выберите нужный раздел: ', reply_markup=menu.admibro)
    else:
        print("\nБот был запущен. ID: " + str(message.chat.id) +
              '    Дата/время: ' + str(datetime.now()))
        bot.send_message(message.chat.id,
                         "Добро пожаловать в Pineapple Shop❗️\n\n◼️ Здесь ты можешь воспользоваться всеми возможными  услугами\n\n◼Огромный выбор услуг и товаров")
        bot.send_message(message.from_user.id,
                         'Выберите нужный раздел: ', reply_markup=menu.start)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,
                     "Список доступных команд:\n\n/start - Для начала работы с ботом\n/help - Список доступных команд\n/info - Узнать информацию о боте\n\n⚙️Этот раздел пока находится в разработке")


@bot.message_handler(commands=['info'])
def send_info(message):
    bot.send_message(message.chat.id, "Shop by PineApple")


@bot.message_handler(commands=['contact'])
def send_contact(message):
    bot.send_message(
        message.chat.id, "📎Контакты:\n\n◼️ Наши проекты - @text\n\nСотрудничество - @azizamakeeva ✔️")


@bot.message_handler(commands=[config.secret_code])
def send_deepweb(message):
    bot.send_message(message.chat.id, "Бот создан разработчиком Makeeva Aziza.")


@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    if message.chat.id == config.admin_id:
        bot.send_sticker(config.admin_id, config.logo_stick)
    else:
        bot.send_message(message.chat.id, "❌ В доступе отказано!")


@bot.message_handler(commands=['send'])
def send_sticker(message):
    if message.chat.id == config.admin_id:
        for user in joinedUsers:
            bot.send_message(user, message.text[message.text.find(' '):])
    else:
        bot.send_message(message.chat.id, "❌ В доступе отказано!")


@bot.message_handler(commands=['balance'])
def send_balance(message):
    if message.chat.id == config.admin_id:
        api = QApi(token=config.token_qiwi, phone=config.qiwi)
        balance = api.balance[0]
        bot.send_message(config.admin_id, "🥝 Баланс вашего Киви: *" +
                         str(balance) + "* руб", parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "❌ В доступе отказано!")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == '⬅️ Назад':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.keyboard)
        elif call.data == '🛒Услуги':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.koret)
        elif call.data == 'Химчистка':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Самая лучшая химчистка в городе!\nЦена? - обговаривается индивидуально с менеджером.️")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == 'Такси':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="🚖Быстрое, надежное такси\n\nЦена - как 2 кофе☕\n\nРекомендуйте друзьям - получайте их 20% на карту")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == 'Клининг':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="🔶Быстро и чисто!\n\n🔷ГЛОБАЛЬНАЯ ЧИСТОТА!\n\nЦена обговаривается индивидуально.")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)

        elif call.data == 'Жодежда':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="👑 Брендовые вещи за 50% стоимости\n\nЧасы, одежда, аксессуары и многое другое всегда в наличии.\nЕсли нужна какая-то определенная вещь или аксессуар - пишите нашему менеджеру\n\nВСЯ ОДЕЖДА НОВАЯ И ОРИГИНАЛЬНАЯ")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == 'Связь':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="🔍 О! Твой лучший оператор! \n\n-Детализация номера\n-Пополнить баланс\n- Заказать sim-карту")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)

        elif call.data == '📚Книги':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.zxc)
        elif call.data == 'CестраКерри':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📚Книги📚\n\nНазвание: Cестра Керри  \n\nОписание: Восемнадцатилетняя Каролина (Керри) Мибер едет из родного маленького городка Колумбия-сити к старшей сестре и её мужу в Чикаго. И родственники, и город встречают её неласково. С трудом найденную после долгих поисков тяжёлую работу на фабрике Керри потеряла из-за болезни. \n\nЦена: 500 сом.")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == 'Америка':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📚Книги📚\n\nНазвание: Американская трагедия  \n\nОписание: Роман Американская трагедия - вершина творчества выдающегося американского писателя Теодора Драйзера. Он говорил: Никто не создает трагедий - их создает жизнь. Писатели лишь изображают их. Драйзеру удалось так талантливо изобразить трагедию Клайда Грифитса, что его история не оставляет равнодушным и современного читателя. Молодой человек, вкусивший всю прелесть жизни богатых, так жаждет утвердиться в их обществе, что идет ради этого на преступление. \n\nЦена: 750 рублей")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == 'Финансист':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📚Книги📚\n\nНазвание: Финансист  \n\nОписание: Финансист - первая часть знаменитой -Трилогии желания- Теодора Драйзера, в основу которой положена история жизни американского миллионера Чарльза Йеркса, сыгравшего значительную роль в разработке системы общественного транспорта в Чикаго и Лондонского метрополитена.\n\nЦена: 320 рублей")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == 'Стоик':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="""📚Книги📚\n\nНазвание: Стоик  \n\nОписание: "Стоик"- третья, заключительная часть знаменитой "Трилогии желания" Теодора Драйзера, в основу которой положена история жизни американского миллионера Ч. Йеркса, сыгравшего значительную роль в разработке системы общественного транспорта в Чикаго и Лондонского метрополитена.\n\nЦена: 510 сом """)
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == 'Гений':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📚Книги📚\n\nНазвание: Гений \n\nОписание: История талантливого художника Юджина Витлы западает в душу также глубоко, как и жизнь Фрэнка Каупервуда (Трилогия желаний) и трагедия Клайда Гриффитса (Американская трагедия).Жизнь Юджина соткана из творчества и страстей, из любви к женщинам и любви к живописи, из запретов и их нарушений, из головокружительного успеха и горьких падений.Жизненный путь Юджина, описанный в романе, Драйзер разделяет на три этапа: юность, борьба, бунт. 'Гений' в отличие от двух других названных романов не заканчивается смертью главного героя, и у читателя есть возможность представить дальнейшую его судьбу. Такая незаконченность романа не отпускает от него очень долго.\n\nЦена: 340 cом")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == '💳 Карты':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.rich)
        elif call.data == 'Кыргызстан Банк':
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'Оптима':
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'Финка':
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'Халык':
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'KICB':
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == '🗂Обучение':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.typer)
        elif call.data == 'МУЗЫКА':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="🎵МУЗЫКА\n\nСписок курсов:\n\n-Курс по классу Фортепиано\n-Курс по Гитаре\n- FL Studio с нуля \n\nЦена: Курсы по инструменту -  500 сом, FL Studio - 200 сом.  ")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == '3D МОДЕЛИРОВАНИЕ':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="🖌3D МОДЕЛИРОВАНИЕ\n\nСписок курсов:\n\n- Дмитрий Смирнов - Онлайн-курс 3D моделирование для начинающих в 3ds max (2019)\n- [Blender3D] Артём Слаква - Курс по основам Blender 2.8+ (2019)\n\nЦена: 300 сом.")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == 'РАЗРАБОТКА':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="👾ПРОГРАММИРОВАНИЕ\n\nСписок курсов:\n\n-Геймдизайн: как делать игры, которые нравятся и приносят деньги (2019)\n- [Udemy] Создание игры на Unity и C# | Полный курс| 2D Space Shooter (2019)\n\nЦена: 170 сом.")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == '🎮Игры':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.gopa)

        elif call.data == '🍔Еда':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.linux)

        elif call.data == 'GTA':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text="🎮Название: Grand Theft Auto: San Andreas \n\nGrand Theft Auto: San Andreas — компьютерная игра в жанре action-adventure, разработанная студией Rockstar North и изданная компанией Rockstar Games; пятая по счёту и третья трёхмерная игра во франшизе Grand Theft Auto.")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == 'Counter':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text="🎮Название: Counter-Strike\n\nCounter-Strike — серия компьютерных игр в жанре командного шутера от первого лица, основанная на движке GoldSrc и выросшая из одноимённой модификации игры Half-Life.")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.oplati)
        elif call.data == '📱Анонимный телефон':
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'Макдональдс':
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=False, text="К сожалению, Макдональдс не работает в данной области.")
        elif call.data == 'БургерКинг':
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=False, text="К сожалению, Бургер Кинг не работает в данной области.")

        elif call.data == '💻 Анонимный ноутбук':
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == '🕹 Анонимная флешка':
            bot.answer_callback_query(
                callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")

        elif call.data == 'Оплатить':
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          inline_message_id=call.inline_message_id, reply_markup=menu.cash)
        elif call.data == 'Узнать настройки':
            if call.message.chat.id == config.admin_id:
                f = open("config.py", "r")
                bot.send_message(config.admin_id, f.read())
            else:
                bot.send_message(call.message.chat.id, "❌ В доступе отказано!")
        else:
            bot.send_message(
                call.message.chat.id, "Ничего не понятно!\n\nСписок доступных команд /help")


@bot.message_handler(content_types=['text'])
def send_otziv(message):
    if message.text == '💌 Отзывы':
        print('Нажал Отзывы. ID: ' + str(message.chat.id) +
              '    Дата/время: ' + str(datetime.now()))
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Оставить первый отзыв", url="https://t.me/azizamakeeva")
        keyboard.add(url_button)
        bot.send_message(
            message.chat.id, "💌 Отзывы\n\nЧестные отзывы о нашем магазине, по ссылке ниже", reply_markup=keyboard)
    elif message.text == '🏛 Новости':
        print('Нажал Новости. ID: ' + str(message.chat.id) +
              '    Дата/время: ' + str(datetime.now()))
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Присоединиться", url="https://t.me/azizamakeeva")
        keyboard.add(url_button)
        bot.send_message(
            message.chat.id, "❗️Свежие новости КР 🇰🇬 - https://t.me/sputnik_kyrgyzstan",
            reply_markup=keyboard)
    elif message.text == '💼 Контакты':
        print('Нажал Контакты. ID: ' + str(message.chat.id) +
              '    Дата/время: ' + str(datetime.now()))
        bot.send_message(
            message.chat.id, "📎Контакты:\n\n◼️ Наши проекты - @kakoito_krutoi_proekt\n\nУслуги гаранта(5%) - @azizamakeeva ✔️")

    elif message.text == '🗂 Каталог товаров':
        print('Нажал Каталог. ID: ' + str(message.chat.id) +
              '    Дата/время: ' + str(datetime.now()))
        bot.send_message(
            message.chat.id, "Что мы можем вам предложить?", reply_markup=menu.keyboard)
    elif message.text == '👤 Мой кабинет':
        print('Нажал Кабинет. ID: ' + str(message.chat.id) +
              '    Дата/время: ' + str(datetime.now()))
        bot.send_message(message.chat.id, "👤 Личный кабинет\n\nНикнейм: " +
                         message.chat.username + "\nID: " + str(message.chat.id) + "\nЯзык: Ru")
    elif message.text == '🔥АДМИН ПАНЕЛЬ🔥':
        if message.chat.id == config.admin_id:
            bot.send_message(
                config.admin_id, "☎️ Админ панель", reply_markup=menu.abc)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '💰Баланс':
        if message.chat.id == config.admin_id:
            api = QApi(token=config.token_qiwi, phone=config.qiwi)
            balance = api.balance[0]
            bot.send_message(config.admin_id, "🥝 Баланс вашего Киви: *" +
                             str(balance) + "* руб", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '📈Статистика':
        if message.chat.id == config.admin_id:
            bot.send_message(config.admin_id, "🔨Этот раздел еще в разработке")
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '🦋Стикеры':
        if message.chat.id == config.admin_id:
            bot.send_sticker(config.admin_id, config.logo_stick)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '⬅️ Назад':
        if message.chat.id == config.admin_id:
            bot.send_message(
                config.admin_id, '⬅️ Вы вернулись в главное меню', reply_markup=menu.admibro)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '😈Админы':
        if message.chat.id == config.admin_id:
            bot.send_message(
                config.admin_id, '🧊Список Админов: 🧊\n\n@admin', reply_markup=menu.nice)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '🛒 Добавить товар':
        if message.chat.id == config.admin_id:
            bot.send_message(config.admin_id, '🔨Этот раздел еще в разработке')
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '📩 Рассылка':
        if message.chat.id == config.admin_id:
            bot.send_message(
                config.admin_id, "Выберите нужное действие", reply_markup=menu.krekin)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == 'Отправить новое сообщение':
        if message.chat.id == config.admin_id:
            bot.send_message(config.admin_id,
                             "Начнем!\n\nВы можете отправить подписчикам одно или несколько сообщений, в том числе любые файлы, музыку,картинки и т.д\n\nДля того, чтобы сделать рассылку нажмите /send и введите ваше сообщение.",
                             reply_markup=menu.krekin)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '🛍 Мои покупки':
        bot.send_message(message.chat.id, '🎉 Мои покупки:')
    else:
        bot.send_message(
            message.chat.id, "Ничего не понятно!\n\nСписок доступных команд /help")


if __name__ == '__main__':
    bot.polling(none_stop=True)

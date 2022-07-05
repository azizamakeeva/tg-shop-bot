import telebot
from telebot import types

start = telebot.types.ReplyKeyboardMarkup(True, False)
start.row('🗂 Каталог товаров')
start.row('💌 Отзывы', '🏛 Новости','💼 Контакты')

admibro = telebot.types.ReplyKeyboardMarkup(True, False)
admibro.row('🗂 Каталог товаров', '👤 Мой кабинет')
admibro.add('🔥АДМИН ПАНЕЛЬ🔥')
admibro.row('🛍 Мои покупки', '💼 Контакты')
admibro.row('💌 Отзывы', '🏛 Новости')

abc = telebot.types.ReplyKeyboardMarkup(True, False)
abc.row('💰Баланс', '📈Статистика')
abc.row('😈Админы', '🛒 Добавить товар')
abc.row('📩 Рассылка', '🦋Стикеры')
abc.add('⬅️ Назад')

krekin = telebot.types.ReplyKeyboardMarkup(True, False)
krekin.row('Отправить новое сообщение')
krekin.row('⬅️ Назад')
# каталог товаров
keyboard = types.InlineKeyboardMarkup()
but_2 = types.InlineKeyboardButton(text="📚Книги", callback_data="📚Книги")
but_1 = types.InlineKeyboardButton(text="💳 Карты", callback_data="💳 Карты")
but_3 = types.InlineKeyboardButton(text="🛒Услуги", callback_data="🛒Услуги")
but_4 = types.InlineKeyboardButton(text="🗂Обучение", callback_data="🗂Обучение")
but_5 = types.InlineKeyboardButton(text="🎮Игры", callback_data="🎮Игры")
but_6 = types.InlineKeyboardButton(text="🍔Еда", callback_data="🍔Еда")
keyboard.row(but_1, but_2)
keyboard.row(but_3)
keyboard.row(but_4, but_5)
keyboard.row(but_6)


rich = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Кыргызстан Банк", callback_data="Кыргызстан Банк")
but_2 = types.InlineKeyboardButton(text="Оптима", callback_data="Оптима")
but_3 = types.InlineKeyboardButton(text="Финка", callback_data="Финка")
but_4 = types.InlineKeyboardButton(text="Халык", callback_data="Халык")
but_5 = types.InlineKeyboardButton(text="KICB", callback_data="KICB")
but_6 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
rich.row(but_1)
rich.row(but_2)
rich.row(but_3)
rich.row(but_4)
rich.row(but_5)
rich.row(but_6)

typer = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="МУЗЫКА", callback_data="МУЗЫКА")
but_2 = types.InlineKeyboardButton(text="3D МОДЕЛИРОВАНИЕ", callback_data="3D МОДЕЛИРОВАНИЕ")
but_3 = types.InlineKeyboardButton(text="ПРОГРАММИРОВАНИЕ", callback_data="РАЗРАБОТКА")
but_4 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
typer.row(but_1)
typer.row(but_2)
typer.row(but_3)
typer.row(but_4)

linux = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="🍟Макдональдс", callback_data="Макдональдс")
but_2 = types.InlineKeyboardButton(text="🍦Бургер Кинг", callback_data="БургерКинг")
but_3 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
linux.row(but_1)
linux.row(but_2)
linux.row(but_3)


gopa = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="GTA - San Andreas", callback_data="GTA")
but_2 = types.InlineKeyboardButton(text="Counter-Strike", callback_data="Counter")
but_3 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
gopa.row(but_1)
gopa.row(but_2)
gopa.row(but_3)

koret = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="🧴Химчистка", callback_data="Химчистка")
but_2 = types.InlineKeyboardButton(text="🚕Такси ", callback_data="Такси")
but_3 = types.InlineKeyboardButton(text="🧼Клининг", callback_data="Клининг")
but_4 = types.InlineKeyboardButton(text="👔Женская одежда", callback_data="Жодежда")
but_5 = types.InlineKeyboardButton(text="📱Сотовая связь", callback_data="Связь")
but_7 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
koret.row(but_5)
koret.row(but_2)
koret.row(but_1)
koret.row(but_4)
koret.row(but_3)
koret.row(but_7)

zxc = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Теодор Драйзер - Сестра Керри", callback_data="СестраКерри")
but_2 = types.InlineKeyboardButton(text="Теодор Драйзер - Американская история", callback_data="Америка")
but_3 = types.InlineKeyboardButton(text="Теодор Драйзер - Финансист", callback_data="Финансист")
but_4 = types.InlineKeyboardButton(text="Теодор Драйзер - Стоик", callback_data="Стоик")
but_5 = types.InlineKeyboardButton(text="Теодор Драйзер - Гений", callback_data="Гений")
but_6 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
zxc.row(but_2)
zxc.row(but_3)
zxc.row(but_4)
zxc.row(but_5)
zxc.row(but_1)
zxc.row(but_6)

oplati = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Оплатить", url="https://t.me/azizamakeeva")
but_2 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
oplati.row(but_1)
oplati.row(but_2)

nice = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Узнать настройки", callback_data="Узнать настройки")
nice.row(but_1)
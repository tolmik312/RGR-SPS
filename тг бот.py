import telebot
from telebot import types

# Инициализация бота с указанием токена
bot = telebot.TeleBot('6714894668:AAFegiM5l390t534pOhUW5aSAfdSuJa40Vw')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Напиши /otel, чтобы узнать занятость номеров.")

# Обработчик команды /schedule
@bot.message_handler(commands=['otel'])
def handle_schedule(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button_yes = types.InlineKeyboardButton(text="посмотрел", callback_data="yes")
    callback_button_no = types.InlineKeyboardButton(text="хочу забронировать номер", callback_data="no")
    keyboard.add(callback_button_yes, callback_button_no)
    bot.send_message(message.chat.id, "Информация о занятости номеров доступно по ссылке: <https://f3c0-92-37-143-179.ngrok-free.app>", reply_markup=keyboard)

# Обработчик нажатия кнопок
@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Вы посмотрели информацию о занятости номеров. Если хотите забронировать номер в отеле, нажмите 'Хочу забронировать номер'")
        # Отправка ответа разработчику или иной логики
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 
                         "Напишите /bron, если хотите узнать информацию о бронировании номера. "
                         "Если вы хотите вернуться к началу, напишите /start")

# Обработчик команды /bron
@bot.message_handler(commands=['bron'])
def handle_report(message):
    bot.send_message(message.chat.id, "Для бронирования номера звоните по номеру +8888888888 для возврата в начало напишите /start ")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_report(message):
    handle_start(message)

# Обработчик всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    bot.send_message(message.chat.id, "Прости, я не понимаю тебя. Попробуй другую команду.")

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)

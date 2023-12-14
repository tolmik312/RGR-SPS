Данный телеграмм-бот предназначен людей которые хотят забронировать номер в отеле,или посмотерть занятость номеров. Бот помогает оптимизировать процесс бронирования номера. клиентам позволяет удобно посмотреть занятость номеров , и бронировать номер, а разработчику удобно принимать заказы на аренду номера в отеле.

ЗАПУСК НА ЛОКАЛЬНОЙ МАШИНЕ

Чтобы запустить бота на локальной машине, необходимо вставить id бота в телеграмм, а затем запустить код бота в среде предназначенной для Python. Ссылка на бота [https://web.telegram.org/k/#@OtelrgrBot]

КАК ПОЛЬЗОВАТЬСЯ БОТОМ

При запуске бота необходимо написать "/start"
После необходимо написат команду "/otel"
Перейдя по ссылке и ознакомившись с занятостью номеров, необходимо нажать одну из кнопок "Посмотерл" или "Хочу забронировать номер"
После нажатия на кнопку "Хочу забронировать номер" необходимо написать команду "/bron"
После бронирования номера для возврата назад, нужно нажать на кнопку "/start"
КОД БОТА import telebot
from telebot import types
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

КОНТАКТНАЯ ИНФОРМАЦИЯ

GitHub [https://github.com/tolmik312] Email [tolmaf123@gmail.com]

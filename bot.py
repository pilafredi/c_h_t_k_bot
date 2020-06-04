# -*- coding: utf-8 -*-
import telebot
import urllib.request as unllib2

# токен боту
bot = telebot.TeleBot('1130800870:AAEeQ6SZvJP9gYFotYOKMfUuvn9oeLU27XQ')

# функція яка визиває "клавіатуру" з кнопками
@bot.message_handler(commands=['start'])
def handler_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Розклад', )
    user_markup.row('Посилання на сайт', )
    user_markup.row('', )
    user_markup.row('Група МС-42', )
    bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)

# функція яка визиває "клавіатуру" з кнопками
@bot.message_handler(content_types=['text'])
def handler_text(message):
    if message.text == 'Група МС-42':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/42.jpg'
        unllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == 'Група МС-14':
        url = 'http://www.chtk.ck.ua/main/images/Rozklad/II_sem/14.jpg'
        unllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

# не дає зупинити бота при виникненні помилки
bot.polling(none_stop=True)

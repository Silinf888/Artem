import telebot

TOKEN = '7201761674:AAFPmXTmHdeBCqrWYL_5SrdONhs6Rfb3zyY'
bot = telebot.TeleBot(TOKEN)

# Слова-триггеры и ответы
responses = {
    "Артем": "Пiдорас",
    "Артём": "Пидарас",
    "Artem": "Pidaras",
    "бот": "Скажи Артем",
}

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id  # Универсальный chat ID (для ЛС и групп)
    
    if message.text in responses:
        bot.send_message(chat_id, responses[message.text])  # Отправляем нужный ответ

print("Бот запущен...")
bot.polling(none_stop=True)

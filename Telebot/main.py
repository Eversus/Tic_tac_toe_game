import telebot
from config import currency, TOKEN
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

# Приветствие пользователя
@bot.message_handler(commands=['start', 'help'])
def start(message):
    text = f"Приветствую, {message.chat.first_name}! \n" \
           f"Я ваш персональный помощник и умею конвертировать валюту. \n" \
           f"Пример ввода валюты: \n" \
           f"Доллар Рубль 10 - сколько рублей в 10 долларах \n" \
           f"Хотите увидеть список доступной валюты? \n" \
           f"Для этого введите команду /values! \n" \
           f"Для получения повторной справки введите команду /help"
    bot.send_message(message.chat.id, text)

# Справка о типах валют
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Вы можете запросить информацию по следующим валютам: \n"
    for cur in currency.keys():
        text += cur + '\n'
    bot.reply_to(message, text)

# Получаем конвертируемую валюту через API cryptocompare.com
@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком много параметров')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Неудалось обработать команду\n{e}')
    else:
        text = f'{amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)

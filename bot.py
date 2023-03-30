import telebot
from pycoingecko import CoinGeckoAPI
from telebot import types

coinGecko = CoinGeckoAPI()

token_bot = "6241202899:AAERRY8oDclG-u1NDKFwicLr0KK0cXWujkw"

bot = telebot.TeleBot(token_bot)


@bot.message_handler(commands=["start"])
def main(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton("Получить курс крипты"))
    cr = bot.send_message(message.chat.id, "Главная", reply_markup=b1)
    bot.register_next_step_handler(cr, get_course_token)


def get_course_token(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton("Курс в USD"), types.KeyboardButton(
        "Курс в RUB"), types.KeyboardButton("Главная"))
    q = bot.send_message(message.chat.id, "Курс токенов", reply_markup=b1)
    bot.register_next_step_handler(q, parse_course)


def parse_course(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton("Перейти"))
    if message.text == "Курс в USD":
        price = coinGecko.get_price(
            ids="bitcoin, ethereum, litecoin, monero, uniswap ", vs_currencies="usd")
        bot.send_message(message.chat.id, f"Bitcoin = {price['bitcoin']['usd']} $\n"
                                          f"Ethereum = {price['ethereum']['usd']} $\n"
                                          f"Litecoin = {price['litecoin']['usd']} $\n"
                                          f"Monero = {price['monero']['usd']} $\n"
                                          f"Uniswap = {price['uniswap']['usd']} $\n", reply_markup=b1)
        go_main = bot.send_message(
            message.chat.id, "Вернуться назад?", reply_markup=b1)
        bot.register_next_step_handler(go_main, get_course_token)
    elif message.text == "Курс в RUB":
        price = coinGecko.get_price(
            ids="bitcoin, ethereum, litecoin,monero, uniswap ", vs_currencies="rub")
        bot.send_message(message.chat.id, f"Bitcoin = {price['bitcoin']['rub']} ₽ \n"
                                          f"Ethereum = {price['ethereum']['rub']} ₽ \n"
                                          f"Litecoin = {price['litecoin']['rub']} ₽ \n"
                                          f"Monero = {price['monero']['rub']} ₽ \n"
                                          f"Uniswap = {price['uniswap']['rub']} ₽ \n", reply_markup=b1)
        go_main = bot.send_message(
            message.chat.id, "Вернуться назад?", reply_markup=b1)
        bot.register_next_step_handler(go_main, get_course_token)
    elif message.text == "Главная":
        main(message)


bot.polling()

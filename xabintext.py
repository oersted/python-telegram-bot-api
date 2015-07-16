from time import sleep
from telegram_bot import TelegramBot, Keyboard

bot = TelegramBot("118437580:AAGXUgcC4tY5pZKKTNGAuWao105j771eBK8")
while(True):
    bot.update()
    while(bot.has_next()):
        next = bot.next()
        if next.text.startswith("/cheese"):
            bot.send_message(next.chat, "pizza")
        elif next.text.startswith("/satel"):
            bot.send_sticker(next.chat, "BQADBAAD4QADxVlzAAJrUse1K2NwAg")
        elif next.text.startswith("/aukerak"):
            keyboard = Keyboard([["/cheese", "/satel"]], True)
            bot.send_message(next.chat, "a", keyboard=keyboard)
    sleep(0.1)

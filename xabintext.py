from time import sleep
from telegram_bot import TelegramBot

bot = TelegramBot("118437580:AAGXUgcC4tY5pZKKTNGAuWao105j771eBK8")
while(True):
    bot.update()
    while(bot.has_next()):
        next = bot.next()
        if next.text.startswith("/cheese"):
            bot.send_message(next.chat, "pizza")
    sleep(0.1)

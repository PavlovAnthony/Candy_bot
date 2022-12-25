#Здесь создается бот и хранится его токен

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

#объект бота
bot = Bot(token='Token')
#диспетчер
dp = Dispatcher(bot)
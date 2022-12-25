# Cюда все функции отправляющие сообщения

from aiogram import types
from bot import bot
import commands
import model

async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'На столе лежит 117 конфет. Играют два игрока, делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. \n'
                           f'Ваш противник БОТ - первый ход обределяется жеребьевкой /draw')

async def end (message: types.Message):
    if model.winner == 1:
        await bot.send_message(message.from_user.id,
                            f' До свидания, {message.from_user.first_name}!')
    
async def drawResult (message: types.Message):
    if model.draw == 1:
        await bot.send_message(message.from_user.id,
                        f' Первым ходит {message.from_user.first_name}')
    else:
        await bot.send_message(message.from_user.id,
                        f' Первым ходит БОТ')
        
async def showTotal (message: types.Message):
        await bot.send_message(message.from_user.id,
                        f' Осталось {model.count} конфет')

async def showBotSteep (message: types.Message):
        await bot.send_message(message.from_user.id,
                        f'{commands.steepBot}')

async def showWinner (message: types.Message):
    if model.winner == 1:
        await bot.send_message(message.from_user.id,
                        f' Выиграл {message.from_user.first_name}\n'
                        f' Сыграть еще - нажмите /draw \n'
                        f' Закончить играть /finish ')
    else:
        await bot.send_message(message.from_user.id,
                        f' Выиграл БОТ \n'
                        f' Сыграть еще, нажмите /draw \n'
                        f' Закончить играть /finish ')

async def wrongNumber (message: types.Message):
        await bot.send_message(message.from_user.id, 'Ах, ты грязный читер!')

async def wrongText (message: types.Message):
        await bot.send_message(message.from_user.id, 'Введите число от 1 до 28')
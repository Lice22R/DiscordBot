import discord
from discord.ext import commands

import logging

from dotenv import load_dotenv
import os


# Подгружаем переменные окружения из файла .env
load_dotenv()


# Основные токены
APPLICATION_ID = os.getenv('APPLICATION_ID')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TOKEN = os.getenv('TOKEN')


# Настройки бота
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
client.intents.members = True


PLACEHOLDER = 'В какие игры вы играете?'
CHOOSEN_GAMES = [
    {
        'label': 'DayZ',
        'description': 'А ты вышел из Беты?',
        'emoji': '🧟',
        'value': 'dayz',
    },
    {
        'label': 'Valorant',
        'description': 'Снова с одной тычки в голову?',
        'emoji': '🔫',
        'value': 'valorant',
    },
    {
        'label': 'WarThunder',
        'description': 'Есть пробитие!',
        'emoji': '✈️',
        'value': 'warthunder',
    },
    {
        'label': 'Dota 2',
        'description': 'А я все думал, когда же ты появишься!',
        'emoji': '🔞',
        'value': 'dota2',
    },
    {
        'label': 'Apex',
        'description': 'Бутербродница',
        'emoji': '🤖',
        'value': 'apex',
    },
    {
        'label': 'Овердрочь',
        'description': 'Руки на стол!',
        'emoji': '🥛',
        'value': 'overwhatch',
    },
    {
        'label': 'Эшкрек фром Краков',
        'description': 'В гоооолову!',
        'emoji': '⚰️',
        'value': 'escapefromtarkov',
    },
    {
        'label': 'CS',
        'description': 'А ты уже купил новые читы?',
        'emoji': '💣',
        'value': 'cs',
    },
    {
        'label': 'Rocket League',
        'description': 'Врум врумм мазафака!!!',
        'emoji': '💨',
        'value': 'rocketleague',
    },
]

ROLE_ASSOCIATIONS = {
    'dayz': '1216493809978970184',
    'valorant': '1216494174010998904',
    'warthunder': '1216494790779338854',
    'dota2': '1216493979269595148',
    'apex': '1216494246727651389',
    'overwhatch': '1216518517667663902',
    'escapefromtarkov': '1216494071489499206',
    'cs': '1216494478358085652',
    'rocketleague': '1216494700521853038',
}

STARTING_ROLE_ID = '1216498611068604498'


# Настройки логера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

logger.addHandler(file_handler)

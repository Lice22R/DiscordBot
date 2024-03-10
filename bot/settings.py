import discord
from discord.ext import commands
import logging


# Основные токены
APPLICATION_ID = '1216025052764704799'
PUBLIC_KEY = 'd47b0580994bcade173be2ef41cb47bc4eeac1fa79a04973a26dbe4c082b6b24'
CLIENT_SECRET = 'jtUGFwSWApMTrsf9C4lDsvbIy93lLRdg'
TOKEN = 'MTIwOTU1MDg5MjQxNjYzOTA0Ng.GJTILW.YlUmckiCAm3LAW0J_6hZ3ZtbmhOy4ggyyjVRcw'


# Настройки бота
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

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

#Список всех ролей по их id
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

#Роль выдающаяся всем при входе
STARTING_ROLE = '1216498611068604498'

# Настройки логера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

logger.addHandler(file_handler)

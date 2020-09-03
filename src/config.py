import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
PREFIX = os.getenv('PREFIX')
RIOT_TOKEN = os.getenv('RIOT_TOKEN')
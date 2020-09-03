import discord
from discord.ext import commands
import config

client = commands.Bot(command_prefix=config.PREFIX, description="This is a Python Bot")

# Events

# Event for success connection
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

# Fix: No Funciona
# Intento querer que descarte los mensajes de otros bots.
# @client.event
# async def on_message(message):
#     if message.author.bot:
#         return

# Commands
# Standard Command Syntaxis
@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Initialization with token
client.run(config.TOKEN)
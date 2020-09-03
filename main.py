import discord
import os
import constants

#Set bot Online mode
client = discord.Client()

print(constants.BOT_TOKEN)

client.run(constants.BOT_TOKEN)
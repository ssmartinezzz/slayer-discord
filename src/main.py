from discord.ext import commands
from discord.ext.commands import CommandNotFound
import discord
import datetime
import time

from objects.player import Player

# Import config file
import config


# Initialize the bot
description = "This is a Python Bot"

bot = commands.Bot(command_prefix=config.PREFIX, description=description)
start_time = time.time()


# Event for success connection
@bot.event
async def on_ready():
    print("------")
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


# Handle errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Command not found!")


@bot.command(description="Pong!")
async def ping(ctx):
    """Pong!"""
    await ctx.send("Pong!")


@bot.command()
async def server(ctx):
    """Get info for the server"""
    embed = discord.Embed(description="Bienvenidos a la Grieta", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_author(name=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
    embed.add_field(name="Server created at:", value=f"{ctx.guild.created_at}", inline=True)
    embed.add_field(name="Server Owner:", value=f"{ctx.guild.owner}", inline=True)
    embed.add_field(name="Server Region:", value=f"{ctx.guild.region}", inline=True)
    embed.add_field(name="Server ID:", value=f"{ctx.guild.id}", inline=True)
    embed.set_footer(text=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embed)


@bot.command()
async def opgg(ctx, *args):
    """Pull up op.gg for players"""
    url = "http://las.op.gg/"

    if len(args) == 1:
        url += "summoner/userName=" + args[0]
    elif len(args) > 1:
        url += "summoner/userName=" + args[0]
        for i in range(1, len(args)):
            url += "+" + args[i]

    await ctx.send(url)


@bot.command()
async def uptime(ctx):
    """How long has Discord Bot been alive? """
    await ctx.send(str(int(time.time() - start_time)) + ' segundos.')


if __name__ == "__main__":
    print("Loading dependencies...")
    modules = ["summoners"]
    for module in modules:
        try:
            bot.load_extension("modules." + module)
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(module, exc))

    bot.run(config.TOKEN)

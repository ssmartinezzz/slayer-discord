import discord
from discord.ext import commands
from objects.player import Player
from requests import HTTPError
from riotwatcher import RiotWatcher
import config

watcher = RiotWatcher(config.RIOT_TOKEN)
default_region = 'la2'


class Summoners(commands.Cog):
    def __init__(self, bot):
        """ TODAVIA NO ANDA """
        
        self.bot = bot

    @commands.command(name='info')
    async def get_summoner(self, ctx, name: str):
        """Display information on a summoner"""
        try:
            player = Player(name)
        except HTTPError as err:
            await ctx.send('Failed to fetch summoner! Error code {}'.format(err.response.status_code))
            return

        try:
            embed = discord.Embed()
            embed.add_field(name="Summoner:", value=f"{player.name}", inline=True)
            print(player.name)
            await ctx.send(embed=embed)
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load embed!\n{}".format(exc))
        else:
            ret = 'Name: ' + player.name + '\n'
            ret += '\tLevel: ' + player.summoner_level + '\n'
            ret += '\tRanked: \n'
            ret += '\t\tSolo/Duo - ' + player.solo_rank + '\n'
            ret += '\t\tFlex 5v5 - ' + player.flex_rank + '\n'
            ret += '\t\tFlex 3v3 - ' + player.threes_rank

            await ctx.send(ret)


def setup(bot):
    bot.add_cog(Summoners(bot))

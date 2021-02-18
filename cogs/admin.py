import discord
from discord.ext import commands

from lib.instant import Instant
from lib.player import Players



class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.instant = Instant(bot)
        self.players = Players()


    @commands.command()
    async def status(self,ctx):
        await ctx.send(self.bot.system.status)

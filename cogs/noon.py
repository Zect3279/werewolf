import discord
from discord.ext import commands




class Noon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def make(self,ctx):
        print("make")




def setup(bot):
    bot.add_cog(Noon(bot))

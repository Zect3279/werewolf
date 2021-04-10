import discord
from discord.ext import commands


class Noon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.system = bot.system

    async def start(self):
        print("[START]: noon")
        chan = discord.utils.get(self.bot.system.guild.text_channels, name="会議所")
        await chan.send("昼が開始しました。\n誰を追放するかの会議を開始してください。")

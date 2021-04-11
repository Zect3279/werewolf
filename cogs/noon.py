import asyncio

import discord
from discord.ext import commands


class Noon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.system = bot.system

    async def start(self):
        print("[START]: noon")
        self.system.status = "noon"
        chan = discord.utils.get(self.bot.system.guild.text_channels, name="会議所")
        msg = await chan.send("昼が開始しました。\n誰を追放するかの会議を開始してください。")
        NUM = 10
        for i in range(NUM):
            n = NUM - i
            txt = "■" * n
            await msg.edit(txt)
            await asyncio.sleep(0.9)
        await chan.send("昼が終了しました。\n今日追放するかの投票を行います。")
        print("[END]: noon")

import discord
from discord.ext import commands

import asyncio

from cogs.night import Night
from cogs.noon import Noon


class GameMaster(commands.Cog):
    def __init__(self, bot):
        self.role_list: list
        self.bot = bot
        self.system = bot.system
        self.night = Night(bot)
        self.noon = Noon(bot)

    def ro_li(self):
        role_list = []
        for p in self.bot.system.player.live:
            role_list.append(p.role)
        return role_list

    async def start(self):
        role_list = self.ro_li()
        self.chan = discord.utils.get(self.bot.system.guild.text_channels, name="会議所")
        # 勝敗判定
        wolf = 0
        cit = 0
        for p in self.bot.system.player.live:
            if p.role == "人狼":
                wolf += 1
            else:
                cit += 1
        if cit <= wolf:
            await self.wolf_end()
            return
        if wolf == 0:
            await self.cit_end()
            return
        if self.system.status == "night":
            await self.noon.start()
            return
        await self.night.start(role_list)
        await self.start()

    async def wolf_end(self):
        print(f"[GameMaster]: 人狼の勝利")
        await self.chan.send("人狼の勝利")

    async def cit_end(self):
        print(f"[GameMaster]: 市民の勝利")
        await self.chan.send("市民の勝利")

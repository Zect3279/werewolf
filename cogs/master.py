import discord
from discord.ext import commands

import asyncio

from cogs.night import Night
from cogs.noon import Noon

from roles.observe import Observe, Werewolf, Fortun


class GameMaster(commands.Cog):
    def __init__(self, bot):
        self.role_list: list
        self.bot = bot
        self.observe = Observe(bot)
        self.wolf = Werewolf(bot)
        self.fortun = Fortun(bot)
        self.night = Night(bot)
        self.noon = Noon(bot)

    async def start(self, role_list):
        # 勝敗判定
        await self.night.start(role_list)
        await self.noon.start()

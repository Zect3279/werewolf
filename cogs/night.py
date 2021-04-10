import discord
from discord.ext import commands

import asyncio

from roles.observe import Observe, Werewolf, Fortun


class Night(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.observe = Observe(bot)
        self.wolf = Werewolf(bot)
        self.fortun = Fortun(bot)

    async def start(self, role_list):
        print("[START]: night")
        print("check")
        await asyncio.gather(
            self.wolf.check(role_list),
            self.fortun.check(role_list),
        )
        print("while")
        await self.Await()

    async def Await(self):
        await asyncio.sleep(1)
        if self.bot.system.wolf.can_move:
            await self.Bwait()
        elif self.bot.system.fortun.can_move:
            await self.Bwait()
        else:
            await self.mo()

    async def Bwait(self):
        await asyncio.sleep(1)
        if self.bot.system.wolf.can_move:
            await self.Await()
        elif self.bot.system.fortun.can_move:
            await self.Await()
        else:
            await self.mo()

    async def mo(self):
        print("move")
        await asyncio.gather(
            self.wolf.move(),
            self.fortun.move(),
        )
        # await self.end.finish()
        print("[END]: night")


def setup(bot):
    bot.add_cog(Night(bot))

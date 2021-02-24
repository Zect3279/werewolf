import discord
from discord.ext import commands
import asyncio

from lib.player import Players
from lib.setting import Set
from lib.instant import Instant

from roles.observe import Observe, Werewolf, Fortun
# from roles.whiling import Willing



class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_list = []
        self.player = Players()
        self.set = Set(bot)
        self.instant = Instant(bot)
        self.observe = Observe(bot)
        self.wolf = Werewolf(bot)
        self.fortun = Fortun(bot)
        # self.whilling = Willing(bot)


    async def deploy(self,ctx,players):
        self.bot.system.players = self.player.make_data(players)
        self.bot.system.player.live = self.bot.system.players
        await self.set.roles()
        await self.instant.add()
        self.bot.system.on = True
        await self.move()
        await self.set.channels()
        await self.channel()
        await self.every()
        await self.call()
        await self.ro_li()
        role_list = self.role_list
        print("check")
        await asyncio.gather(
        self.wolf.check(role_list),
        self.fortun.check(role_list),
        )
        print("while")
        await self.observe.wait()

    async def mo(self):
        print("move")
        await asyncio.gather(
        self.wolf.move(),
        self.fortun.move(),
        )
        print("Finish")


    async def move(self):
        for p in self.bot.system.players:
            mem = self.bot.system.guild.get_member(p.id)
            role = discord.utils.get(self.bot.system.guild.roles, name="生存者")
            await mem.add_roles(role)
            chan = discord.utils.get(self.bot.system.guild.voice_channels, name="移動用")
            await mem.edit(voice_channel=chan)


    async def channel(self):
        for p in self.bot.system.players:
            mem = self.bot.system.guild.get_member(p.id)
            role = await self.bot.system.guild.create_role(name=mem.name)
            if p.role == "市民":
                await mem.add_roles(role)
                continue
            chan = discord.utils.get(self.bot.system.guild.text_channels, name=p.role)
            await chan.set_permissions(role,read_messages=True)
            await mem.add_roles(role)


    async def every(self):
        channel = discord.utils.get(self.bot.system.guild.text_channels, name="会議所")
        await channel.send("@everyone\n全員に役職を付与しました。\nそれぞれの専用チャンネルにてメンションが飛びます。\n確認してください。\n（市民の方にはメンションは飛んでません）")

    async def call(self):
        for p in self.bot.system.players:
            if p.role == "市民":
                continue
            channel = discord.utils.get(self.bot.system.guild.text_channels, name=p.role)
            await channel.send(f"<@{p.id}> あなたは、 __{p.role}__ です。")

    async def ro_li(self):
        for p in self.bot.system.player.live:
            self.role_list.append(p.role)
        print(self.role_list)

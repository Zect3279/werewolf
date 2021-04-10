import discord
from discord.ext import commands
import asyncio

from cogs.master import GameMaster
from cogs.night import Night

from lib.player import Players
from lib.setting import Set
from lib.instant import Instant
from lib.end import End

from roles.observe import Observe, Werewolf, Fortun


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_list = []
        self.player = Players()
        self.set = Set(bot)
        self.instant = Instant(bot)
        self.observe = Observe(bot)
        self.wolf = Werewolf(bot)
        self.fortun = Fortun(bot)
        self.end = End(bot)
        self.master = GameMaster(bot)

    async def deploy(self, ctx):
        self.role_list = []
        players = self.player.give_role(self.bot.system.player.all)
        print(players)
        self.bot.system.player.all = players
        for p in self.bot.system.player.all:
            print(p.id)
        self.bot.system.player.live = self.bot.system.player.all
        await self.set.roles()
        await self.instant.add()
        self.bot.system.on = True
        print("[VC]: ON")
        await self.set.channels()
        await self.channel(ctx)
        await self.ro_li()
        await self.move()
        await self.every()
        await self.call()
        role_list = self.role_list
        await self.master.start(role_list)
        return

    async def move(self):
        print(self.bot.system.player.all)
        for p in self.bot.system.player.all:
            mem = self.bot.system.guild.get_member(p.id)
            role = discord.utils.get(self.bot.system.guild.roles, name="生存者")
            await mem.add_roles(role)
            chan = discord.utils.get(self.bot.system.guild.voice_channels, name="移動用")
            await mem.edit(voice_channel=chan)

    async def channel(self, ctx):
        all_role = ctx.guild.roles
        for p in self.bot.system.player.all:
            mem = self.bot.system.guild.get_member(p.id)
            print(f"[{mem.name}]: {p.role}")
            role = discord.utils.get(all_role, name=mem.name)
            if role:
                await role.delete()
            role = await self.bot.system.guild.create_role(name=mem.name)
            if p.role == "市民":
                await mem.add_roles(role)
                continue
            chan = discord.utils.get(self.bot.system.guild.text_channels, name=p.role)
            await chan.set_permissions(role, read_messages=True)
            await mem.add_roles(role)

    async def every(self):
        channel = discord.utils.get(self.bot.system.guild.text_channels, name="会議所")
        await channel.send("@everyone\n全員に役職を付与しました。\nそれぞれの専用チャンネルにてメンションが飛びます。\n確認してください。\n（市民の方にはメンションは飛んでません）")

    async def call(self):
        for p in self.bot.system.player.all:
            if p.role == "市民":
                continue
            channel = discord.utils.get(self.bot.system.guild.text_channels, name=p.role)
            await channel.send(f"<@{p.id}> あなたは、 __{p.role}__ です。")

    async def ro_li(self):
        for p in self.bot.system.player.live:
            self.role_list.append(p.role)
        print(self.role_list)

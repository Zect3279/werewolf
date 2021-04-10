# start.py

import discord
from discord.ext import commands

from typing import Any


class Instant:
    def __init__(self, bot: Any):
        self.bot = bot

    async def all(self, ctx):
        all_role = ctx.guild.roles
        for rol in all_role:
            try:
                await rol.delete()
            finally:
                a = "a"

        for chan in ctx.guild.channels:
            await chan.delete()

        await ctx.guild.create_text_channel("welcome")

        category = await ctx.guild.create_category(name="総合")
        await ctx.guild.create_role(name="全体チャット")
        await category.create_text_channel("全体チャット")
        voice = await category.create_voice_channel("全体チャット")
        await voice.edit(user_limit=99)

    async def dele(self, ctx):
        all_role = ctx.guild.roles
        for rol in all_role:
            try:
                if rol.name == "人狼参加者":
                    await rol.delete()
                if rol.name == "生存者":
                    await rol.delete()
                if rol.name == "死亡者":
                    await rol.delete()
                if rol.name == "観戦者":
                    await rol.delete()
            finally:
                a = "a"

        for p in self.bot.system.player.live:
            mem = self.bot.system.guild.get_member(p.id)
            print(mem)
            role = discord.utils.get(all_role, name=mem.name)
            print(role)
            await role.delete()
            # try:
            # except:
            #     continue

        for p in self.bot.system.player.dead:
            mem = self.bot.system.guild.get_member(p.id)
            print(mem)
            role = discord.utils.get(all_role, name=mem.name)
            print(role)
            await role.delete()

        channel = discord.utils.get(ctx.guild.voice_channels, name='移動用')
        for chan in channel.category.channels:
            await chan.delete()
        await channel.category.delete()
        channel = discord.utils.get(ctx.guild.text_channels, name='観戦')
        for chan in channel.category.channels:
            await chan.delete()
        await channel.category.delete()
        channel = discord.utils.get(ctx.guild.text_channels, name='反省会')
        for chan in channel.category.channels:
            await chan.delete()
        await channel.category.delete()

        channel = discord.utils.get(ctx.guild.text_channels, name='人狼')
        for chan in channel.category.channels:
            await chan.delete()
        await channel.category.delete()
        channel = discord.utils.get(ctx.guild.text_channels, name='会議所')
        for chan in channel.category.channels:
            await chan.delete()
        await channel.category.delete()

    async def make(self, ctx):
        all_role = ctx.guild.roles
        for rol in all_role:
            if rol.name == "人狼参加者":
                self.bot.system.role.on = discord.utils.get(all_role, name="人狼参加者")
            if rol.name == "生存者":
                self.bot.system.role.alive = discord.utils.get(all_role, name="生存者")
            if rol.name == "死亡者":
                self.bot.system.role.killed = discord.utils.get(all_role, name="死亡者")
            if rol.name == "観戦者":
                self.bot.system.role.no = discord.utils.get(all_role, name="観戦者")

        if not self.bot.system.role.on:
            self.bot.system.role.on = await ctx.guild.create_role(name="人狼参加者")

        if not self.bot.system.role.alive:
            self.bot.system.role.alive = await ctx.guild.create_role(name="生存者")

        if not self.bot.system.role.killed:
            self.bot.system.role.killed = await ctx.guild.create_role(name="死亡者")

        if not self.bot.system.role.no:
            self.bot.system.role.no = await ctx.guild.create_role(name="観戦者")

        # self.mems = await lol.cho(self.mems)

        category = await ctx.guild.create_category(name="人狼ゲーム")
        voice = await category.create_voice_channel("移動用")
        await voice.edit(user_limit=50)

        category = await ctx.guild.create_category(name="生存者")
        chan = await category.create_text_channel("会議所")
        await chan.set_permissions(ctx.guild.roles[0], read_messages=False)
        await chan.set_permissions(self.bot.system.role.on, read_messages=True)
        voice = await category.create_voice_channel("会議所")
        await voice.edit(user_limit=50)
        await voice.set_permissions(ctx.guild.roles[0], connect=False, speak=False)

        category = await ctx.guild.create_category(name="役職")
        chan = await category.create_text_channel("人狼")
        await chan.set_permissions(ctx.guild.roles[0], read_messages=False)
        await chan.set_permissions(self.bot.system.role.killed, read_messages=True)
        await chan.set_permissions(self.bot.system.role.no, read_messages=True)

        category = await ctx.guild.create_category(name="死亡者")
        chan = await category.create_text_channel("反省会")
        await chan.set_permissions(ctx.guild.roles[0], read_messages=False)
        await chan.set_permissions(self.bot.system.role.killed, read_messages=True)
        voice = await category.create_voice_channel("反省会")
        await voice.edit(user_limit=50)
        await voice.set_permissions(ctx.guild.roles[0], connect=False)

        category = await ctx.guild.create_category(name="不参加者")
        chan = await category.create_text_channel("観戦")
        await chan.set_permissions(ctx.guild.roles[0], read_messages=False)
        await chan.set_permissions(self.bot.system.role.no, read_messages=True)
        voice = await category.create_voice_channel("観戦中")
        await voice.edit(user_limit=99)
        await voice.set_permissions(ctx.guild.roles[0], connect=False)

    async def add(self):
        channel = discord.utils.get(self.bot.system.guild.text_channels, name='人狼')
        category = channel.category
        for p in self.bot.system.player.all:
            role = p.role
            if role == "人狼":
                continue

            chan = discord.utils.get(self.bot.system.guild.text_channels, name=role)
            if not chan:
                chan = await category.create_text_channel(role)
            await chan.set_permissions(self.bot.system.guild.roles[0], read_messages=False)
            await chan.set_permissions(self.bot.system.role.killed, read_messages=True)
            await chan.set_permissions(self.bot.system.role.no, read_messages=True)

# start.py

import discord
from discord.ext import commands

from typing import Any



class Instant():
    def __init__(self, bot: Any):
        self.bot = bot

    async def dele(self,ctx):
        all_role = ctx.guild.roles
        for rol in all_role:
            try:
                await rol.delete()
            except:
                a = "a"
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

    async def make(self,ctx):
        self.bot.system.role.on = await ctx.guild.create_role(name="人狼参加者")
        self.bot.system.role.live = await ctx.guild.create_role(name="生存者")
        self.bot.system.role.dead = await ctx.guild.create_role(name="死亡者")
        self.bot.system.role.no = await ctx.guild.create_role(name="観戦者")

        # self.mems = await lol.cho(self.mems)

        category = await ctx.guild.create_category(name="人狼ゲーム")
        voice = await category.create_voice_channel("移動用")
        await voice.edit(user_limit=50)

        category = await ctx.guild.create_category(name="生存者")
        chan = await category.create_text_channel("会議所")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(self.bot.system.role.on,read_messages=True)
        voice = await category.create_voice_channel("会議所")
        await voice.edit(user_limit=50)
        await voice.set_permissions(ctx.guild.roles[0],connect=False,speak=False)

        category = await ctx.guild.create_category(name="役職")
        chan = await category.create_text_channel("人狼")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(self.bot.system.role.dead,read_messages=True)
        await chan.set_permissions(self.bot.system.role.no,read_messages=True)

        category = await ctx.guild.create_category(name="死亡者")
        chan = await category.create_text_channel("反省会")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(self.bot.system.role.dead,read_messages=True)
        voice = await category.create_voice_channel("反省会")
        await voice.edit(user_limit=50)
        await voice.set_permissions(ctx.guild.roles[0],connect=False)

        category = await ctx.guild.create_category(name="不参加者")
        chan = await category.create_text_channel("観戦")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(self.bot.system.role.no,read_messages=True)
        voice = await category.create_voice_channel("観戦中")
        await voice.edit(user_limit=99)
        await voice.set_permissions(ctx.guild.roles[0],connect=False)

    async def add(self):
        channel = discord.utils.get(self.bot.system.guild.text_channels, name='人狼')
        category = channel.category
        for p in self.bot.system.players:
            role = p.role
            if role == "人狼":
                continue
            chan = await category.create_text_channel(role)
            await chan.set_permissions(self.bot.system.guild.roles[0],read_messages=False)
            await chan.set_permissions(self.bot.system.role.dead,read_messages=True)
            await chan.set_permissions(self.bot.system.role.no,read_messages=True)

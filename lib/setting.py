import discord
from discord.ext import commands


class Set:
    def __init__(self, bot):
        self.bot = bot

    async def channels(self):
        channels = self.bot.system.guild.text_channels
        self.bot.system.channel.cit = discord.utils.get(channels, name="市民")
        self.bot.system.channel.wolf = discord.utils.get(channels, name="人狼")
        self.bot.system.channel.fortun = discord.utils.get(channels, name="占い師")

    async def roles(self):
        roles = self.bot.system.guild.roles
        self.bot.system.role.on = discord.utils.get(roles, name="人狼参加者")
        self.bot.system.role.alive = discord.utils.get(roles, name="生存者")
        self.bot.system.role.killed = discord.utils.get(roles, name="死亡者")
        self.bot.system.role.no = discord.utils.get(roles, name="観戦者")

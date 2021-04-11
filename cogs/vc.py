import discord
from discord.ext import commands


class VC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        GUILD = 720566804094648330
        print(f"[VC]: {member.name} を確認")
        if not self.bot.system.on:
            return
        if before.channel == after.channel:
            return
        if before.channel:
            if before.channel.guild.id != GUILD:
                return
            cname = before.channel.name
            if cname == "観戦中":
                role = discord.utils.get(before.channel.guild.roles, name="観戦者")
                await member.remove_roles(role)
                return

        if after.channel:
            if after.channel.guild.id != GUILD:
                return
            cname = after.channel.name
            if not cname.startswith("移動用"):
                return
            role = discord.utils.get(after.channel.guild.roles, name="生存者")
            if role in member.roles:
                channel = discord.utils.get(after.channel.guild.voice_channels, name="会議所")
                await member.edit(voice_channel=channel)
                return
            role = discord.utils.get(after.channel.guild.roles, name="死亡者")
            if role in member.roles:
                channel = discord.utils.get(after.channel.guild.voice_channels, name="反省会")
                await member.edit(voice_channel=channel)
                return
            channel = discord.utils.get(after.channel.guild.voice_channels, name="観戦中")
            role = discord.utils.get(after.channel.guild.roles, name="観戦者")
            await member.edit(voice_channel=channel)
            await member.add_roles(role)
            return


def setup(bot):
    bot.add_cog(VC(bot))

import discord
from discord.ext import commands


class VC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):
        if self.on == False:
            return
        if before.channel == after.channel:
            return
        try:
            if before.channel.guild.id != 726233332655849514:
                return
            cname = before.channel.name
            if cname != "観戦中":
                return
            role = discord.utils.get(before.channel.guild.roles, name="観戦者")
            await member.remove_roles(role)
            # print(f"{self.times} [Connection] : Removed {member.name} `s '観戦者'")
        except:
            a = "a"
        finally:
            try:
                if after.channel.guild.id != 726233332655849514:
                    return
                cname = after.channel.name
                if cname != "移動用":
                    return
                role = discord.utils.get(after.channel.guild.roles, name="生存者")
                if role in member.roles:
                    channel = discord.utils.get(after.channel.guild.voice_channels, name="会議所")
                    await member.edit(voice_channel=channel)
                    # print(f"{self.times} [Connection] : {member.name} has connected into '会議所'")
                    return
                role = discord.utils.get(after.channel.guild.roles, name="死亡者")
                if role in member.roles:
                    channel = discord.utils.get(after.channel.guild.voice_channels, name="反省会")
                    # print(f"{self.times} [Connection] : {member.name} has connected into '反省会'")
                    await member.edit(voice_channel=channel)
                    return
                channel = discord.utils.get(after.channel.guild.voice_channels, name="観戦中")
                role = discord.utils.get(after.channel.guild.roles, name="観戦者")
                await member.edit(voice_channel=channel)
                # print(f"{self.times} [Connection] : {member.name} has connected into '観戦中'")
                await member.add_roles(role)
            except:
                a = "a"
            finally:
                a = "a"



def setup(bot):
    bot.add_cog(VC(bot))

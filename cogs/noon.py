import asyncio

import discord
from discord.ext import commands


class Noon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.system = bot.system

    async def start(self):
        print("[START]: noon")
        self.system.status = "noon"
        chan = discord.utils.get(self.bot.system.guild.text_channels, name="会議所")
        msg = await chan.send("昼が開始しました。\n誰を追放するかの会議を開始してください。")
        NUM = 10
        for i in range(NUM):
            n = NUM - i
            txt = "■" * n
            await msg.edit(txt)
            await asyncio.sleep(0.9)
        await chan.send("昼が終了しました。\n今日追放するかの投票を行います。")
        self.bot.system.status = "vote"
        VOTETIME = 10
        msg = await chan.send(f"`/vote <@role>` で投票を完了してください。\n残り時間：{VOTETIME}")
        for i in range(VOTETIME):
            n = VOTETIME - i
            await msg.edit(f"`/vote <@role>` で投票を完了してください。\n残り時間：{n}")
        await msg.edit("投票時間が終了しました。\n投票を開示します。")
        vote_list = ""
        for user_id in self.bot.system.vote:
            user = self.bot.get_user(user_id)
            member = self.system.vote[user_id]
            vote_list += f"{user.name} => {member.name}\n"
        await chan.send(f"```\n{vote_list}```")
        print("[END]: noon")

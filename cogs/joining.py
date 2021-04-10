import discord
from discord.ext import commands

import asyncio

from lib.player import Player


class Joining(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        if self.bot.system.status != "recruiting":
            return
        if ctx.author in self.bot.system.player.all:
            return
        print(f"{ctx.author.name} join")
        player = Player(ctx.author.id)
        self.bot.system.player.all.append(player)
        role = discord.utils.get(ctx.guild.roles, name="人狼参加者")
        await ctx.author.add_roles(role)
        await ctx.message.add_reaction("⭕")

    async def count(self, ctx, count: int = 10):
        print("count")

        await ctx.send("開始を確認...\n参加希望の方は、`/join` と入力し、\nVC[総合チャット]に参加してください。")
        edit = await ctx.send(f"開始まで{count}秒")
        self.bot.system.status = "recruiting"
        for i in range(count):
            num = count - i
            await edit.edit(content=f"開始まで{num}秒")
            await asyncio.sleep(0.9)
        self.bot.system.status = "preparing"
        await ctx.send("募集を終了しました。\n開始まで少々お待ちください。")


def setup(bot):
    bot.add_cog(Joining(bot))

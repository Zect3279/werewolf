import discord
from discord.ext import commands

from cogs.joining import Joining
from cogs.game import Game

from lib.instant import Instant


class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.players = []
        self.instant = Instant(bot)
        self.joining = Joining(bot)
        self.starting = Game(bot)

    @commands.Cog.listener()
    async def on_ready(self):
        print("I am ready")

    @commands.command()
    async def start(self, ctx, n=10):
        print("start")
        self.bot.system.__init__()

        channels = ctx.guild.text_channels
        channel = discord.utils.get(channels, name="観戦")
        if not channel:
            print("make")
            await self.instant.make(ctx)
        self.players = await self.joining.count(ctx, n)
        await ctx.send(self.bot.system.player.all)
        if not self.bot.system.player.all:
            await ctx.send("no one")
            return
        # if len(self.players) <= 3:
        #     await ctx.send("参加を希望したのが3名以下だったため、開始できません。\n停止します...")
        #     return
        # txt = "参加者一覧\n```\n"
        # for user in self.players:
        #     txt += f"・{user.name}\n"
        # await ctx.send(f"{txt}```")
        self.bot.system.guild = ctx.guild
        await self.starting.deploy(ctx)


def setup(bot):
    bot.add_cog(Start(bot))

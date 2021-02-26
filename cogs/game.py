import discord
from discord.ext import commands

from cogs.controll import Controll
from cogs.start import Start

from lib.instant import Instant



class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.players = []
        self.instant = Instant(bot)
        self.controll = Controll(bot)
        self.starting = Start(bot)


    @commands.Cog.listener()
    async def on_ready(self):
        print("I am ready")

    @commands.command()
    async def delete(self,ctx):
        print("delete")
        await self.instant.all(ctx)

    @commands.command()
    async def make(self,ctx):
        print("make")
        await self.instant.make(ctx)

    @commands.command()
    async def reset(self,ctx):
        print("reset")
        await self.instant.dele(ctx)

    @commands.command()
    async def start(self,ctx):
        print("start")
        self.players = await self.controll.count(ctx)
        await ctx.send(self.bot.system.players)
        if not self.bot.system.players:
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
        await self.starting.deploy(ctx,self.bot.system.players)




def setup(bot):
    bot.add_cog(Game(bot))

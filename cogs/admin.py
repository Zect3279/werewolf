import discord
from discord.ext import commands

from lib.instant import Instant
from lib.player import Players


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.instant = Instant(bot)
        self.players = Players()

    @commands.command()
    async def delete(self, ctx):
        print("delete")
        await self.instant.dele(ctx)
        self.bot.system.__init__()

    @commands.command()
    async def make(self, ctx):
        print("make")
        await self.instant.make(ctx)

    @commands.command()
    async def reset(self, ctx):
        print("reset")
        self.bot.system.__init__()
        await self.instant.all(ctx)

    @commands.command()
    async def status(self, ctx):
        await ctx.send(self.bot.system.status)

    @commands.command()
    async def players(self, ctx):
        await ctx.send(self.bot.system.player.all)

    @commands.command()
    async def live(self, ctx):
        await ctx.send(self.bot.system.player.live)

    @commands.command()
    async def dead(self, ctx):
        await ctx.send(self.bot.system.player.dead)

    @commands.command()
    async def roles(self, ctx):
        roles = []
        for p in self.bot.system.player.live:
            roles.append(p.role)
        await ctx.send(roles)

    @commands.command()
    async def role(self, ctx):
        for p in self.bot.system.player.live:
            if ctx.author.id == p.id:
                player = p
        await ctx.send(player.role)

    @commands.command()
    async def guild(self, ctx):
        await ctx.send(self.bot.system.guild)

    async def cog_before_invoke(self, ctx):
        if ctx.author.id != 653785595075887104:
            return


def setup(bot):
    bot.add_cog(Admin(bot))

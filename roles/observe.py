import discord
from discord.ext import commands


class Observe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.wolf = Werewolf(bot)
        self.fortun = Fortun(bot)

    async def box(self, chan, title):
        txt = "A. 誰も選択しない"
        for i, p in enumerate(self.bot.system.player.all):
            txt += f"\n{self.count[i]}. <@{p.id}>"

        test = discord.Embed(title=title, colour=0x1e90ff)
        test.add_field(name=title, value=txt, inline=True)
        msg = await chan.send(embed=test)

        await msg.add_reaction('🇦')
        for i, p in enumerate(self.bot.system.player.all):
            await msg.add_reaction(self.ment[i])


class Werewolf(Observe):
    def __init__(self, bot):
        self.bot = bot
        self.count = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
        self.ment = ["🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮", "🇯", "🇰", "🇱", "🇲", "🇳", "🇴", "🇵", "🇶",
                     "🇷", "🇸", "🇹", ]

    async def check(self, roles):
        if "人狼" not in roles:
            print("not wolf")
            self.bot.system.wolf.can_move = False
            return
        self.bot.system.wolf.can_move = True
        print("yes wolf")
        await self.bot.system.channel.wolf.send("殺害する人を指定してください。\n`/raid @[殺害対象名]` で指定できます。")
        # await super().box(self.bot.system.channel.wolf,"殺害する人を選択してください。")

    async def move(self):
        mem = self.bot.system.wolf.flag
        print("kill")
        if mem is None:
            print("mem==none")
            return
        for p in self.bot.system.player.live:
            if p.id != mem.id:
                print("p.id!=mem.id")
                continue
            self.bot.system.player.live.remove(p)
            self.bot.system.player.dead.append(p)
        await mem.remove_roles(self.bot.system.role.alive)
        await mem.add_roles(self.bot.system.role.killed)
        await self.bot.system.channel.wolf.send(f"<@{mem.id}> の殺害が完了しました。")
        chan = discord.utils.get(self.bot.system.guild.voice_channels, name="移動用")
        await mem.edit(voice_channel=chan)
        return


class Fortun(Observe):
    def __init__(self, bot):
        self.bot = bot
        self.count = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
        self.ment = ["🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮", "🇯", "🇰", "🇱", "🇲", "🇳", "🇴", "🇵", "🇶",
                     "🇷", "🇸", "🇹", ]

    async def check(self, roles):
        if "占い師" not in roles:
            print("not fortun")
            self.bot.system.fortun.can_move = False
            return
        self.bot.system.fortun.can_move = True
        print("yes fortun")
        await self.bot.system.channel.fortun.send("占う人を指定してください。\n`/fortun @[占い対象名]` で指定できます。")
        # await super().box(self.bot.system.channel.fortun,"占う人を選択してください。")

    async def move(self):
        mem = self.bot.system.fortun.flag
        print("look")
        if mem is None:
            print("mem==none")
            return
        for p in self.bot.system.player.live:
            if p.id != mem.id:
                print("p.id!=mem.id")
                continue
            if p.role == "人狼":
                bw = "黒"
            else:
                bw = "白"
            await self.bot.system.channel.fortun.send(f"<@{mem.id}> は __{bw}__ です")
        return


def setup(bot):
    bot.add_cog(Observe(bot))

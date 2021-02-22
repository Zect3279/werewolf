import discord
from discord.ext import commands


class Observe(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.wolf = Werewolf(bot)
        self.fortun = Fortun(bot)

    @commands.Cog.listener()
    async def on_reaction_add(self,reaction,user):
        if self.bot.system.move_wait == False:
            return
        u_id = user.id
        id_list = []
        for p in self.bot.system.players:
            id_list.append(p.id)
        if u_id not in id_list:
            return
        for p in self.bot.system.players:
            if p.role == "人狼":
                print("wolf")
                if self.bot.system.wolf.can_move == True:
                    return
                self.bot.system.wolf.can_move = False
                if str(reaction.emoji) == '🇦':
                    await self.bot.system.channel.wolf.send(f"誰も殺害しませんでした。")
                    self.bot.system.wolf.flag = None
                    return
                else:
                    await self.bot.system.channel.wolf.send(f"<@{user.id}> を殺害します。")
                    self.bot.system.wolf.flag = user
                    return
            if p.role == "占い師":
                print("fortun")
                if self.bot.system.fortun.can_move == True:
                    return
                self.bot.system.fortun.can_move = False
                if str(reaction.emoji) == '🇦':
                    await self.bot.system.channel.fortun.send(f"誰も占いませんでした。")
                    self.bot.system.fortun.flag = None
                    return
                else:
                    await self.bot.system.channel.fortun.send(f"<@{user.id}> を占います。")
                    self.bot.system.fortun.flag = user
                    return


    async def box(self,chan,title):
        txt = "A. 誰も選択しない"
        for i, p in enumerate(self.bot.system.players):
            txt += f"\n{self.count[i]}. <@{p.id}>"

        test = discord.Embed(title=title,colour=0x1e90ff)
        test.add_field(name=title, value=txt, inline=True)
        msg = await chan.send(embed=test)

        await msg.add_reaction('🇦')
        for i, p in enumerate(self.bot.system.players):
            await msg.add_reaction(self.ment[i])


class Werewolf(Observe):
    def __init__(self,bot):
        self.bot = bot
        self.count = ["B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
        self.ment = ["🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳","🇴","🇵","🇶","🇷","🇸","🇹",]

    async def check(self,roles):
        if "人狼" not in roles:
            print("not wolf")
            self.bot.system.wolf.can_move = False
            return
        self.bot.system.can_move = True
        print("yes wolf")
        await super().box(self.bot.system.channel.wolf,"殺害する人を選択してください。")


    async def move(self):
        mem = self.bot.system.wolf.flag
        print("kill")
        if mem == None:
            print("mem==none")
            return
        for p in self.bot.system.player.live:
            if p.id != mem.id:
                print("p.id!=mem.id")
                continue
            self.bot.system.player.live.remove(p)
            self.bot.system.player.dead.append(p)
        await mem.remove_roles(self.system.role.live)
        await mem.add_roles(self.bot.system.role.dead)
        await self.channel.wolf.send(f"<@{mem.id}> の殺害が完了しました。")


class Fortun(Observe):
    def __init__(self,bot):
        self.bot = bot
        self.count = ["B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
        self.ment = ["🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳","🇴","🇵","🇶","🇷","🇸","🇹",]

    async def check(self,roles):
        if "占い師" not in roles:
            print("not fortun")
            self.bot.system.fortun.can_move = False
            return
        self.bot.system.can_move = True
        print("yes fortun")
        await super().box(self.bot.system.channel.fortun,"占う人を選択してください。")


    async def move(self):
        mem = self.bot.system.fortun.flag
        print("look")
        if mem == None:
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
            await self.channel.fortun.send(f"<@{mem.id}> は __{bw}__ です")


def setup(bot):
    bot.add_cog(Observe(bot))

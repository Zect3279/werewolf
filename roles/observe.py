import discord
from discord.ext import commands


class Observe(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.wolf = Werewolf(bot)
        self.fortun = Fortun(bot)

    @commands.Cog.listener()
    async def on_reaction_add(self,reaction,user):
        print("called")
        u_id = user.id
        id_list = []
        for p in self.bot.system.players:
            id_list.append(p.id)
        if u_id not in id_list:
            print("role return")
            return
        for p in self.bot.system.players:
            if p.role == "人狼":
                print("wolf")
                if self.wolf.can_move == True:
                    return
                self.wolf.can_move = False
                if str(reaction.emoji) == '🇦':
                    await self.channel_wolf.send(f"誰も殺害しませんでした。")
                    self.wolf.flag = None
                    return
                else:
                    await self.bot.system.channel.wolf.send(f"<@{user.id}> を殺害します。")
                    self.wolf.flag = user
                    return
            if p.role == "占い師":
                print("fortun")
                if self.fortun.can_move == True:
                    return
                self.fortun.can_move = False
                if str(reaction.emoji) == '🇦':
                    await self.channel_fortun.send(f"誰も占いませんでした。")
                    self.fortun.flag = None
                    return
                else:
                    await self.bot.system.channel.fortun.send(f"<@{user.id}> を占います。")
                    self.fortun.flag = user
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





class Werewolf():
    def __init__(self,bot):
        self.bot = bot
        self.count = ["B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
        self.ment = ["🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳","🇴","🇵","🇶","🇷","🇸","🇹",]
        self.can_move = False
        self.flag = None

    async def check(self,roles):
        if "人狼" not in role:
            print("not wolf")
            return
        self.can_move = True
        await self.observe.box(self.bot.system.channel.wolf,"殺害する人を選択してください。")


    async def move(self):
        mem = self.flag
        print("kill")
        if mem == None:
            return
        for p in self.bot.system.player.live:
            if p.id != mem.id:
                continue
            self.bot.system.player.live.remove(p)
            self.bot.system.player.dead.append(p)
        await mem.remove_roles(self.system.role.live)
        await mem.add_roles(self.bot.system.role.dead)
        await self.channel.wolf.send(f"<@{mem.id}> の殺害が完了しました。")


class Fortun():
    def __init__(self,bot):
        self.bot = bot
        self.count = ["B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
        self.ment = ["🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳","🇴","🇵","🇶","🇷","🇸","🇹",]
        self.can_move = False
        self.flag = None

    async def fortun(self,role):
        if "占い師" not in role:
            print("not fortun")
            return
        self.can_move = True
        await self.observe.box(self.channel_fortun,"占う人を選択してください。")


    async def move(self):
        mem = self.flag
        print("look")
        if mem == None:
            return
        for p in self.bot.system.player.live:
            if p.id != mem.id:
                continue
            if p.role == "人狼":
                bw = "黒"
            else:
                bw = "白"
            await self.channel.fortun.send(f"<@{mem.id}> は __{bw}__ です")

def setup(bot):
    bot.add_cog(Observe(bot))

import discord
from discord.ext import commands



class Willing():
    def __init__(self,bot):
        self.bot = bot

    async def wait(self):
        self.bot.system.move_wait = True
        print("loop start")
        while self.bot.system.move_wait == True:
            if self.bot.system.wolf.can_move == True:
                continue
            if self.bot.system.fortun.can_move == True:
                continue

            print("loop stop")
            self.bot.system.move_wait = False

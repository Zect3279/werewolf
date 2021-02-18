import discord
from discord.ext import commands

from roles.observe import Werewolf, Fortun

class Willing():
    def __init__(self,bot):
        self.bot = bot
        self.wolf = Werewolf(bot)
        self.fortun = Fortun(bot)

    def wait(self):
        self.move_wait = True
        print("loop start")
        while self.move_wait == True:
            if self.wolf.can_move == True:
                continue
            elif self.fortun.can_move == True:
                continue
            else:
                print("false")
                self.move_wait = False

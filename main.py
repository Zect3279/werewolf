import discord
from discord.ext import commands

from os import environ
import sys
from lib.system import System



bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(environ.get('PREFIX', '/')),
    help_command=None,
    intents=discord.Intents.all(),
)
bot.system = System()




extensions = [
    "cogs.game",
    "cogs.controll",
    "cogs.vc",
    "cogs.observe"
]
for extension in extensions:
    bot.load_extension(extension)

bot.run(environ["BOT_TOKEN"])

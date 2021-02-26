import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand, cog_ext, SlashContext
from discord_slash.utils import manage_commands

from os import environ
import sys
from lib.system import System



bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(environ.get('PREFIX', '/')),
    help_command=None,
    intents=discord.Intents.all(),
)
bot.system = System()
bot.slash = SlashCommand(bot, sync_commands=True)



extensions = [
    "cogs.game",
    "cogs.controll",
    "cogs.vc",
    "roles.observe",
    "slash.wolf",
    "slash.fortun",
]
for extension in extensions:
    bot.load_extension(extension)

bot.run(environ["BOT_TOKEN"])

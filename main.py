import discord
from discord.ext import commands
from discord_slash import SlashCommand

from os import environ
from lib.system import System

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(environ.get('PREFIX', '/')),
    help_command=None,
    intents=discord.Intents.all(),
)
bot.system = System()
bot.slash = SlashCommand(bot, sync_commands=True)

extensions = [
    "cogs.admin",
    "cogs.start",
    "cogs.joining",
    "cogs.vc",
    "roles.observe",
    "slash.wolf",
    "slash.fortun",
]
for extension in extensions:
    bot.load_extension(extension)

bot.run(environ["BOT_TOKEN"])

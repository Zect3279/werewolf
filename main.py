from os import environ
import sys



bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(environ.get('PREFIX', '/')),
    help_command=None,
    intents=discord.Intents.all(),
)



extensions = [
    "cogs.test",
]
for extension in extensions:
    bot.load_extension(extension)

bot.run(environ["BOT_TOKEN"])

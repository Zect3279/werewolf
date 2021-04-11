import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

from typing import Optional


class SlashVote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.slash.get_cog_commands(self)  # コマンドを取得する
        # asyncio.create_task(self.bot.slash.sync_all_commands()) # 同期してコマンドがDiscordに出るようにする

    # コマンドの定義はcog_ext.cog_slashデコレータを使う
    @cog_ext.cog_slash(
        name='vote',
        description='追放対象の指定　　role[discord.Role]: ロールメンション',
        guild_ids=[720566804094648330, 808283612105408533, 726233332655849514]
    )
    async def slash_say(self, ctx: SlashContext, role: Optional[discord.Role]):
        # if self.bot.system.status != "vote":
        #     await ctx.send("実行に失敗しました。")
        #     return

        try:
            member = role.members[0]
        except IndexError:
            txt = "誰も指定しませんでした。"
        else:
            txt = f"{member.mention} への投票が完了しました。"
            self.bot.system.vote[ctx.author_id] = member

        await ctx.send(content=txt, hidden=True)  # hidden=Trueで実行した人のみにみえるように

    def cog_unload(self):
        self.bot.slash.remove_cog_commands(self)  # コマンド解放


def setup(bot):
    bot.add_cog(SlashVote(bot))

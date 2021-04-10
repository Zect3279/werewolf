import discord


class End:
    def __init__(self, bot):
        self.bot = bot

    async def finish(self):
        all_role = self.bot.system.guild.roles
        print("finish")

        await self.role_remove(all_role, "人狼参加者")
        await self.role_remove(all_role, "生存者")
        await self.role_remove(all_role, "死亡者")
        await self.role_remove(all_role, "観戦者")

        for p in self.bot.system.player.live:
            mem = self.bot.system.guild.get_member(p.id)
            role = discord.utils.get(all_role, name=mem.name)
            await role.delete()

        for p in self.bot.system.player.dead:
            mem = self.bot.system.guild.get_member(p.id)
            role = discord.utils.get(all_role, name=mem.name)
            await role.delete()

        print("Done!")
        return

    async def role_remove(self, all_role, name):
        role = discord.utils.get(all_role, name=name)
        for mem in role.members:
            print(mem)
            await mem.remove_roles(role)

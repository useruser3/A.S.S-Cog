import discord
from discord.ext import commands
sesh = ""
class Session:
    """My custom cog for A.S.S"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def session(self,ctx):
        """get context"""
        server = ctx.message.server
        await self.bot.say(server.get_channel('434434257348198400').topic)


def setup(bot):
    bot.add_cog(Session(bot))
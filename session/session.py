from discord.ext import commands
channelid = 434434257348198400
class Session:
    """My custom cog"""

    @commands.command(pass_context=True)
    async def session(self,ctx):
        """get context"""
        server = ctx.message.guild
        await ctx.send(server.get_channel(channelid).topic)


from discord.ext import commands
channelid = 434434257348198400
class Session:
    """My custom cog"""

    @commands.group(pass_context=True)
    async def session(self,ctx):
        """get context"""
        if ctx.invoked_subcommand is None:
            server = ctx.message.guild
            await ctx.send(server.get_channel(channelid).topic)

    @session.command(name="set", pass_context=True)
    async def set_session(self,ctx):
        server = ctx.message.guild
        await ctx.send("hello world")
        

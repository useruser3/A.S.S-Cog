from redbot.core import commands
from redbot.core import Config
import discord
acechannel = 474639017422356491

def is_channel(channel_id):
            def predicate(ctx):
                 return ctx.channel.id == channel_id
            return commands.check(predicate)
            return ctx.send("error")
def is_channel_not(channel_id):
            def predicate(ctx):
                 return ctx.channel.id != channel_id
            return commands.check(predicate)
            return ctx.send("error")


class Credits:
    def __init__(self):
        #start config section
        self._config = None
        #end config

    def get_config(self,ctx):
        if self._config is None:
            self._config = ctx.bot.get_cog("Session").config
        return self._config

#credits commands
    @commands.group(autohelp=False)
    async def credits(self,ctx):
        """shows credits for the bot"""
        self.get_config(ctx)
        user_data = self._config.user(ctx.author)
        if ctx.invoked_subcommand is None:
            await ctx.send("My coder was useruser3 and my meowrtist was Sarah Kenny of deviant art and the community of this discord. \nYou can find more of Sarah's work at https://www.deviantart.com/sassie-kay Nya!  ")